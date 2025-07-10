import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QTextEdit, QLineEdit, QPushButton
)
import ollama
import yaml


class AibotUI(QWidget):
    def __init__(self):
        super().__init__()
        self.chat_history = []
        self.load_config()


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
    def load_config(self):
        try:
            with open("config.yaml", "r") as f:
                cfg = yaml.safe_load(f)
                self.model_name = cfg.get("model", "mistral")
                system_prompt = cfg.get("system_prompt", "").strip()
                if system_prompt:
                    self.chat_history.append({"role": "system", "content": system_prompt})
        except Exception as e:
            self.model_name = "mistral"
            print(f"[WARN] config.yaml not loaded: {e}")

        
    def handle_send(self):
        message = self.input_field.text().strip()
        if not message:
            return

        self.chat_log.append(f"<b>You:</b> {message}")
        self.input_field.clear()

        self.chat_history.append({"role": "user", "content": message})

        try:
            response = ollama.chat(
            model=self.model_name,
            messages=self.chat_history)


            reply = response['message']['content']
            self.chat_log.append(f"<b>AI:</b> {reply}")
            self.chat_history.append({"role": "assistant", "content": reply})
        except Exception as e:
            self.chat_log.append(f"<b>Error:</b> {e}")




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
