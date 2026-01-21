🤖 Advanced AI Chatbot (Groq + Streamlit)

An interactive AI chatbot application built with Streamlit and Groq-powered LLaMA models, featuring personality-based responses, model selection, temperature control, and session-aware memory.
This project demonstrates how to design a customizable, production-style conversational AI system using modern LLM APIs.

📌 Project Overview

The Advanced AI Chatbot allows users to interact with Large Language Models through a clean and intuitive web interface.
Users can dynamically control the chatbot’s personality, creativity level, and underlying LLM, making it a flexible platform for experimenting with conversational AI.
The application follows secure API practices and emphasizes real-world AI system design, not just basic prompt usage.

✨ Key Features
🤖 Groq LLM integration (LLaMA models)
🎭 Multiple assistant personalities
🌡️ Adjustable response creativity (temperature)
🔁 Stateful conversation memory
🔄 Live model switching from UI
🗑️ One-click chat history reset
🖥️ Clean and responsive Streamlit chat interface
🔐 Secure API key handling via environment variables

🎭 Supported Personalities
Users can select different AI behaviors using predefined system prompts:

Helpful Assistant
Friendly Companion
Professional Tutor
Tech Expert
Creative Storyteller

This demonstrates prompt engineering and controlled AI behavior.

🧠 Supported Models

llama-3.1-8b-instant
llama-3.1-70b-versatile

Models can be switched dynamically from the sidebar.

🛠️ Tech Stack

Python
Streamlit – Web application framework
Groq API – LLaMA-based LLM inference
Session State – Chat memory management
Prompt Engineering – Personality control

📁 Project Structure

advanced_ai_chatbot/

├── app.py          # Main Streamlit application
├── requirements.txt
└── README.md

⚙️ Installation & Setup

1️⃣ Clone the repository

git clone https://github.com/Areej56/advanced-ai-chatbot.git
cd advanced-ai-chatbot

2️⃣ Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

3️⃣ Install dependencies

pip install -r requirements.txt

🔐 Environment Variables

This project uses the Groq API for LLM inference.

Set your API key securely as an environment variable:

Linux / macOS

export GROQ_API_KEY="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"

Windows

setx GROQ_API_KEY "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"

Advanced AI Chatbot built using Streamlit and Groq’s LLaMA models, designed to provide customizable, personality-driven conversational AI with real-time interaction.

▶️ Run the Application

streamlit run app.py

Open the provided local URL in your browser.

🧪 How It Works

User selects model, personality, and temperature
User enters a message in the chat interface
Conversation history is stored using Streamlit session state
Messages are sent to the Groq LLM API
The chatbot responds according to the selected settings
Chat history persists until reset by the user

🎯 Use Cases

AI chatbot demos
Educational AI tutors
Prompt engineering experiments
Customer support assistants
LLM behavior testing
Conversational AI prototypes

📌 Skills Demonstrated

LLM API integration (Groq)
Prompt engineering & persona design
Stateful conversational systems
Streamlit app development
Secure API key management
AI product prototyping

👩‍💻 Author

Areej Arslan

Machine Learning & Computer Vision Engineer

📍 Lahore, Pakistan


🔗 GitHub: https://github.com/Areej56

⭐ Final Note

This project is designed to reflect industry-level conversational AI development, focusing on usability, customization, and secure integration with modern LLMs.

