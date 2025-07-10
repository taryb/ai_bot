import sys
import os
import json
import yaml
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QTextEdit, QLineEdit, QPushButton
)
import ollama

class AibotUI(QWidget):
    def __init__(self):
        super().__init__()

        self.chat_history = []
        self.model_name = "gemma3:1b"  # fallback

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

        self.load_chat_history()  # ✅ Now it's safe to load and display past messages


    def load_config(self):
        try:
            with open("config.yaml", "r") as f:
                cfg = yaml.safe_load(f)
                self.model_name = cfg.get("model", self.model_name)
                system_prompt = cfg.get("system_prompt", "").strip()
                if system_prompt:
                    self.chat_history.append({"role": "system", "content": system_prompt})
        except Exception as e:
            print(f"[WARN] Could not load config.yaml: {e}")

    def load_chat_history(self):
        try:
            with open("chat_history.json", "r", encoding="utf-8") as f:
                history = json.load(f)
                self.chat_history.extend(history)
                for msg in history:
                    if msg["role"] == "user":
                        self.chat_log.append(f"<b>You:</b> {msg['content']}")
                    elif msg["role"] == "assistant":
                        self.chat_log.append(f"<b>AI:</b> {msg['content']}")
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"[WARN] Could not load chat history: {e}")

    def save_chat_history(self):
        try:
            with open("chat_history.json", "w", encoding="utf-8") as f:
                json.dump(self.chat_history, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"[WARN] Could not save chat history: {e}")

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
                messages=self.chat_history
            )
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
        self.ui = AibotUI()
        self.setCentralWidget(self.ui)

    def closeEvent(self, event):
        self.ui.save_chat_history()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AibotApp()
    window.show()
    sys.exit(app.exec_())
