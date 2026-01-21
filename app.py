import os
import streamlit as st
from groq import Groq
from datetime import datetime


# ⚙️ App Configuration

st.set_page_config(
    page_title="AI Chatbot 🤖",
    page_icon="🧠",
    layout="centered"
)

st.title("🤖 Advanced AI Chatbot")
st.caption("Built with **Groq API + Streamlit** | Enhanced Personality, Memory & Customization")


# 🔐 Load API Key

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("⚠️ GROQ_API_KEY not found. Please set it in your environment variables.")
    st.stop()

# Initialize Groq client
client = Groq(api_key=api_key)


# 🎭 Sidebar: Settings & Personalities

st.sidebar.header("⚙️ Chat Settings")

# Model selection
model = st.sidebar.selectbox(
    "Choose Model:",
    ["llama-3.1-8b-instant", "llama-3.1-70b-versatile"],
    index=0
)

# Temperature control
temperature = st.sidebar.slider(
    "Response Creativity (temperature):",
    min_value=0.1, max_value=1.5, value=0.7, step=0.1
)

# Persona selector
persona = st.sidebar.selectbox(
    "Choose Assistant Personality:",
    ["Helpful Assistant", "Friendly Companion", "Professional Tutor", "Tech Expert", "Creative Storyteller"],
    index=0
)

# Custom system prompt for personality
personality_prompts = {
    "Helpful Assistant": "You are a polite and efficient assistant who answers clearly and helpfully.",
    "Friendly Companion": "You are a warm, humorous friend who speaks casually and empathetically.",
    "Professional Tutor": "You are a patient, knowledgeable teacher who explains concepts step-by-step.",
    "Tech Expert": "You are a confident, concise AI engineer who provides technical insights and code samples.",
    "Creative Storyteller": "You are a playful and imaginative storyteller who makes responses engaging and vivid."
}

system_prompt = personality_prompts[persona]

# Clear chat history button
if st.sidebar.button("🗑️ Clear Chat History"):
    st.session_state.clear()
    st.rerun()


# 💬 Chat Session Initialization

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]


# 📜 Display Chat History

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])

# 🧩 User Input and AI Response

if prompt := st.chat_input("Type your message here..."):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # AI typing animation
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 💭"):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=st.session_state.messages,
                    temperature=temperature,
                )
                reply = response.choices[0].message.content
                st.write(reply)
                # Append assistant reply
                st.session_state.messages.append({"role": "assistant", "content": reply})

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# 🕒 Footer Info

st.markdown("---")
st.markdown(
    f"🧠 **Session Started:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n"
    f"💬 **Model Used:** `{model}` | 🌡️ **Temperature:** `{temperature}`"
)


    
    # GROQ KEY (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)