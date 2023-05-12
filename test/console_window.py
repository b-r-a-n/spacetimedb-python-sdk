from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QTextEdit, QLineEdit, QWidget
from PyQt6.QtGui import QTextCursor, QTextCharFormat, QColor, QIcon

class ConsoleWindow(QMainWindow):
    instance = None
    last_print_was_prompt = False

    def __init__(self, game_controller):
        super().__init__()

        ConsoleWindow.instance = self

        self.game_controller = game_controller

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        self.output_text_edit = QTextEdit()
        self.output_text_edit.setReadOnly(True)
        self.output_text_edit.setStyleSheet("background-color: black; color: white;")
        layout.addWidget(self.output_text_edit)

        self.command_line_edit = QLineEdit()
        
        layout.addWidget(self.command_line_edit)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.command_line_edit.returnPressed.connect(self.process_command)

        self.setWindowTitle("SpacetimeMUD")
        self.setWindowIcon(QIcon("logo.png"))

    def process_command(self):
        command = self.command_line_edit.text()

        self.print(command + "\n")
        
        if self.game_controller.prompt:
            self.game_controller.prompt.command(command)        

        self.command_line_edit.clear()

    def print(self, text, color = "white"):
        char_format = QTextCharFormat()
        char_format.setForeground(QColor(color))

        cursor = self.output_text_edit.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)

        if self.last_print_was_prompt:
            text = '\n\n' + text

        cursor.insertText(text, char_format)

        self.last_print_was_prompt = False

    def prompt(self):
        self.print("> ")
        self.last_print_was_prompt = True