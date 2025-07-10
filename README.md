AI Bot App

A local desktop chatbot built with PyQt5 and powered by Ollama models.

This app gives you a fast, private, and customizable chat experience. It supports local persona prompting via a private YAML config file, allowing you to control the model and tone without touching the code.

⚙️ Features

PyQt5 GUI with input and chat log
Local model integration using Ollama
Private YAML config for model and system prompt
Easily extendable: streaming, persona file loading, chat history
🚀 Setup

1. Clone the repo
git clone https://github.com/taryb/ai_bot.git
cd ai_bot
2. Install dependencies
pip install pyqt5 ollama pyyaml
💡 A virtual environment is optional but recommended for isolated development.
3. Run the app
python3 main.py
Make sure you have an Ollama model installed (like mistral, dolphin3:8b, llama2-uncensored, etc.):

ollama list
📄 What is config.yaml and Why You Need It

The config.yaml file tells the chatbot:

Which Ollama model to use (e.g. mistral, dolphin3:8b, etc.)
What personality or tone to use (optional)
This allows you to define how the chatbot behaves without editing any code.

🔒 The file is private and is not uploaded to GitHub (it’s listed in .gitignore).
🛠 How to Set Up config.yaml

1. In the same folder as main.py, create a file named:
config.yaml
2. Paste in this example (customize as needed):
model: mistral

system_prompt: |
  You are a helpful assistant. Be concise, friendly, and informative.
  Avoid technical jargon unless asked.
3. Ensure .gitignore contains:
config.yaml
✅ That’s it — now your chatbot will use the model and behavior defined in this file.

💡 Tips

You can switch models anytime by editing config.yaml
Leave out system_prompt if you just want default model behavior
If config.yaml is missing or broken, the app defaults to using mistral
📝 Roadmap

 GUI layout and user input
 Ollama model integration
 External YAML config
 Streaming AI responses
 Persona .txt loader
 Save/load chat history
🪪 License

MIT — free to use, modify, and share. Attribution appreciated but not required.

Let me know if you want this turned into a styled PDF again, or ready to commit it.