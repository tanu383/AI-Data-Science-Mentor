import streamlit as st
from google import genai
from dotenv import load_dotenv
import os
load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")

# Gemini Client
client = genai.Client(
    api_key=api_key
)

# Page Config
st.set_page_config(
    page_title="AI Data Science Mentor",
    page_icon="🤖",
    layout="wide"
)

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# CSS Styling
st.markdown("""
<style>

.stApp{
    background-color:#0f172a;
}

.main-title{
    text-align:center;
    color:white;
    font-size:45px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:#cbd5e1;
    font-size:18px;
    margin-bottom:20px;
}

.user-msg{
    background:#2563eb;
    padding:12px;
    border-radius:10px;
    color:white;
    margin:10px 0;
}

.bot-msg{
    background:#1e293b;
    padding:12px;
    border-radius:10px;
    color:white;
    margin:10px 0;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    '<p class="main-title">🤖 AI Data Science Mentor</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Powered by Gemini AI | Python • ML • AI • NLP • Career Guidance</p>',
    unsafe_allow_html=True
)

# User Input
user_input = st.chat_input("Ask me anything about Data Science...")

if user_input:

    # Store User Message
    st.session_state.messages.append(
        {"role":"user","content":user_input}
    )

    prompt = f"""
    You are an AI Data Science Mentor.

    Answer questions related to:
    - Python
    - Data Science
    - Machine Learning
    - Deep Learning
    - NLP
    - AI Engineering
    - Interview Preparation
    - Career Guidance

    User Question:
    {user_input}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    bot_reply = response.text

    st.session_state.messages.append(
        {"role":"assistant","content":bot_reply}
    )

# Display Chat History
for msg in st.session_state.messages:

    if msg["role"] == "user":

        st.markdown(
            f'<div class="user-msg">👩‍💻 {msg["content"]}</div>',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f'<div class="bot-msg">🤖 {msg["content"]}</div>',
            unsafe_allow_html=True
        )

# Clear Chat
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()