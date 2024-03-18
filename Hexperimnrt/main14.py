import streamlit as st
import google.generativeai as genai
import os
from bs4 import BeautifulSoup
import requests

# ... (Existing functions: scrape_webpage, turn_on_switch, turn_off_switch, mul)

# Streamlit app
st.title("Interactive AI Chat App")

# Create a container for chat history
chat_container = st.empty()

# Initialize chat history
chat_history = []

while True:
    user_input = st.text_input("You:", key="user_input")

    if user_input:
        # Add user input to chat history
        chat_history.append({"role": "user", "content": user_input})

        # Send message to the AI and get response
        response = chat.send_message(user_input)

        # Add AI response to chat history
        chat_history.append({"role": "assistant", "content": response.text})

        # Update chat container with the entire history
        chat_container.markdown(
            "\n".join(
                f"{message['role'].capitalize()}: {message['content']}"
                for message in chat_history
            )
        )