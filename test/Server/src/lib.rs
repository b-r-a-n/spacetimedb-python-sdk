pub mod helpers;
pub mod tables;

use std::time::Duration;

use helpers::next_spawnable_entity_id;
use spacetimedb::{rt::log, schedule, spacetimedb, ReducerContext, Timestamp};
use tables::{Exit, ExitDirection, Globals, Location, Mobile, Player, Room, RoomChat};

#[spacetimedb(init)]
pub fn initialize() {
    Globals::insert(Globals {
        id: 0,
        spawnable_entity_id_counter: 0,
    });

    Room::insert(Room {
        room_id: "start".into(),

        name: "Clockwork Labs Lobby".into(),
        description: "    The main lobby of this Silicon Valley startup is an enchanting amalgamation of futuristic eccentricity and vibrant energy. As one steps into the space, they are greeted by a symphony of neon lights dancing across the walls, juxtaposed with sleek, minimalist furniture adorned with plush, oversized cushions in vivid hues.\n    The atmosphere buzzes with the echoes of passionate conversations, the whirring of espresso machines, and the occasional ping-pong ball ricocheting in the air, epitomizing the dynamic spirit of innovation that permeates the company's culture.".into(),
        exits: vec![Exit {
            direction: ExitDirection::NE,
            examine: "An exit".into(),
            destination_room_id: "start".into(),
        }],
        spawnable_entities: Vec::new(),
    });
}

#[spacetimedb(connect)]
pub fn connect(ctx: ReducerContext) {
    if let Some(player) = Player::filter_by_identity(&ctx.sender) {
        schedule!(Duration::ZERO, sign_in(_, player.spawnable_entity_id));
    }
}

#[spacetimedb(disconnect)]
pub fn disconnect(ctx: ReducerContext) {
    if let Some(player) = Player::filter_by_identity(&ctx.sender) {
        schedule!(Duration::ZERO, sign_out(_, player.spawnable_entity_id));
    }
}

#[spacetimedb(reducer)]
pub fn sign_in(_ctx: ReducerContext, player_spawnable_entity_id: u64) -> Result<(), String> {
    let mut location = Location::filter_by_spawnable_entity_id(&player_spawnable_entity_id)
        .unwrap()
        .clone();
    location.room_id = location.last_room_id.clone();
    Location::update_by_spawnable_entity_id(&player_spawnable_entity_id, location);

    Ok(())
}

#[spacetimedb(reducer)]
pub fn sign_out(_ctx: ReducerContext, player_spawnable_entity_id: u64) -> Result<(), String> {
    let mut location = Location::filter_by_spawnable_entity_id(&player_spawnable_entity_id)
        .unwrap()
        .clone();
    location.last_room_id = location.room_id.clone();
    location.room_id = None;
    Location::update_by_spawnable_entity_id(&player_spawnable_entity_id, location);

    Ok(())
}

#[spacetimedb(reducer)]
pub fn create_player(ctx: ReducerContext, name: String, description: String) -> Result<(), String> {
    if Player::filter_by_identity(&ctx.sender).is_some() {
        return Err("Player already exists".into());
    }

    let spawnable_entity_id = next_spawnable_entity_id();

    Location::insert(Location {
        spawnable_entity_id: spawnable_entity_id,
        room_id: Some("start".into()),
        last_room_id: None,
    });
    Mobile::insert(Mobile {
        spawnable_entity_id: spawnable_entity_id,
        name,
        description,
    });
    Player::insert(Player {
        spawnable_entity_id: spawnable_entity_id,
        identity: ctx.sender,
    });

    Ok(())
}

#[spacetimedb(reducer)]
pub fn say(
    ctx: ReducerContext,
    source_spawnable_entity_id: u64,
    chat_text: String,
) -> Result<(), String> {
    if let Some(location) = Location::filter_by_spawnable_entity_id(&source_spawnable_entity_id) {
        if location.room_id.is_some() {
            RoomChat::insert(RoomChat {
                chat_entity_id: 0,

                room_id: location.room_id.unwrap(),
                source_spawnable_entity_id,
                chat_text,

                timestamp: ctx
                    .timestamp
                    .duration_since(Timestamp::UNIX_EPOCH)
                    .unwrap()
                    .as_millis() as u64,
            });
        } else {
            return Err("No location found.".into());
        }
    } else {
        return Err("No mobile found.".into());
    }

    Ok(())
}
