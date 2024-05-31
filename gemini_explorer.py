# from google.cloud import aiplatform
import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

project = "gemini-explorer-424205"
vertexai.init(project=project)

config = generative_models.GenerationConfig(
    temperature=0.3
)
model = GenerativeModel(
    "gemini-pro",
    generation_config=config
)
chat = model.start_chat()

# helper function to display and send streamlit messages
def llm_function(chat, query):
    response = chat.send_message(query)
    output = response.candidates[0].content.parts[0].text

    with st.chat_message("model"):
        st.markdown(output)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    st.session_state.messages.append(
        {
            "role": "model",
            "content": output
        }
    )

st.title("Don GPT")

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display and load to chat history
for index, message in enumerate(st.session_state.messages):
    content = Content(
        role = message["role"],
        parts = Part.from_text(message["content"])
    )

# to capture user input
query = st.chat_input("Write your message here...")

if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(chat, query)

# Capture the user's name
user_name = st.text_input("Please enter your name")

# Check if the user has entered a name
if user_name:
    # Define Don's response with personalized greeting
    rex_response = f"Hello, {user_name}! I'm ReX, an assistant powered by Google Gemini. How can I assist you today?"
    st.write(rex_response)