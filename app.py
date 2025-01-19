import streamlit as st
from main import clarify_text, challenge_text
import time

# Set page configuration
st.set_page_config(
    page_title="Educational AI Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for ChatGPT-like interface
st.markdown("""
    <style>
    /* Main background and layout */
    .stApp {
        background-color: #343541;
        color: #FFFFFF;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #202123;
    }
    
    /* Input area styling */
    .stTextArea textarea {
        background-color: #40414F;
        color: #FFFFFF;
        border: 1px solid #565869;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }
    
    /* Output container styling */
    .output-container {
        background-color: #444654;
        padding: 20px;
        border-radius: 5px;
        margin: 10px 0;
    }
    
    .user-container {
        background-color: #343541;
        padding: 20px;
        border-radius: 5px;
        margin: 10px 0;
    }
    
    /* Button styling */
    .stButton button {
        background-color: #10a37f;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 8px 16px;
        transition: background-color 0.3s;
    }
    
    .stButton button:hover {
        background-color: #1a7f64;
    }
    
    /* Header styling */
    .main-header {
        color: #FFFFFF;
        text-align: center;
        padding: 20px;
        font-size: 24px;
    }
    
    /* Feedback section */
    .feedback-container {
        background-color: #40414F;
        padding: 15px;
        border-radius: 5px;
        margin-top: 20px;
    }
    
    /* Chat history */
    .chat-message {
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
    
    .assistant {
        background-color: #444654;
    }
    
    .user {
        background-color: #343541;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### Settings")
    audience_level = st.selectbox(
        "Select Audience Level",
        ["Beginner", "Intermediate", "Advanced"]
    )
    
    st.markdown("### About")
    st.markdown("""
    This AI educational assistant helps:
    - Simplify complex topics
    - Generate advanced insights
    - Provide examples and definitions
    - Create critical thinking questions
    """)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'feedback_history' not in st.session_state:
    st.session_state.feedback_history = []

# Main content
st.markdown("<h1 class='main-header'>Educational AI Assistant</h1>", unsafe_allow_html=True)

# Input section with audience level
user_input = st.text_area("Enter your text here...", height=100)
col1, col2 = st.columns(2)

def process_and_store(text, mode):
    # Store user input
    st.session_state.chat_history.append({"role": "user", "content": text})
    
    with st.spinner(f'Generating {mode} response...'):
        if mode == "clarify":
            response = clarify_text(text, audience_level.lower())
        else:
            response = challenge_text(text, audience_level.lower())
    
    # Store assistant response
    st.session_state.chat_history.append({"role": "assistant", "content": response})
    return response

# Button handlers
if col1.button("🔍 Clarify", use_container_width=True):
    if user_input:
        process_and_store(user_input, "clarify")
    else:
        st.warning("Please enter some text first!")

if col2.button("🎯 Challenge", use_container_width=True):
    if user_input:
        process_and_store(user_input, "challenge")
    else:
        st.warning("Please enter some text first!")

# Display chat history
for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.markdown(f"<div class='chat-message user'>🧑‍🏫 User: {message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-message assistant'>🤖 Assistant: {message['content']}</div>", unsafe_allow_html=True)

# Feedback section
if st.session_state.chat_history:
    st.markdown("### Feedback")
    with st.container():
        st.markdown("<div class='feedback-container'>", unsafe_allow_html=True)
        feedback_rating = st.slider("Rate the response (1-5)", 1, 5, 3)
        feedback_text = st.text_area("Additional feedback (optional)")
        
        if st.button("Submit Feedback"):
            st.session_state.feedback_history.append({
                "rating": feedback_rating,
                "feedback": feedback_text,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            })
            st.success("Thank you for your feedback!")
        st.markdown("</div>", unsafe_allow_html=True)

# Clear chat button
if st.session_state.chat_history:
    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.experimental_rerun()