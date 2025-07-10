import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QTextEdit, QLineEdit, QPushButton
)

class AibotUI(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.chat_log = QTextEdit()
        self.chat_log.setReadOnly(True)
        layout.addWidget(self.chat_log)

        input_row = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your message...")
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.handle_send)
        self.input_field.returnPressed.connect(self.handle_send)

        input_row.addWidget(self.input_field)
        input_row.addWidget(self.send_button)

        layout.addLayout(input_row)
        self.setLayout(layout)
        def handle_send(self):
            message = self.input_field.text().strip()
            if not message:
                return
            self.chat_log.append(f"<b>You:</b> {message}")
            self.input_field.clear()



class AibotApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Bot")
        self.setGeometry(100, 100, 800, 600)
        self.setCentralWidget(AibotUI())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AibotApp()
    window.show()
    sys.exit(app.exec_())
