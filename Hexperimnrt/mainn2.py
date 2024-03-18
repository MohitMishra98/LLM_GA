import streamlit as st
import os
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# Streamlit app title
st.title("AI Assistant")

# Configure the Google Generative AI
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

# Define the functions for the Google Generative AI model


# def scrape_webpage(url: str):
#     """Scrapes the content of a webpage given its URL."""
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     page_content = soup.get_text(separator=' ', strip=True)
#     return page_content

# def light_switch(state:bool):
#     """can turn on(True) and off(False) a light"""
#     global light_state
#     light_state = state
#     return "turned on lights"

# def mul(a: int, b: int):
#     """Returns multiplication of 2 numbers a and b."""
#     return a * b



# Initialize the light state
light_state = False

# Configure the Google Generative AI model
genai.configure(api_key=GOOGLE_API_KEY)
# model = genai.GenerativeModel("gemini-1.0-pro", tools=[scrape_webpage,light_switch,mul], 
#                               generation_config=generation_config)

model = genai.GenerativeModel("gemini-1.0-pro",
                              generation_config=generation_config)
# Start the chat with the model
chat = model.start_chat(history=[])

# light_indicator_container = st.empty()
# light_indicator = "🔵" if light_state else "🔴"
# light_indicator_container.markdown(
#     f"<div style='position: fixed; bottom: 0; left: 0; margin: 10px; font-size: 30px;'>{light_indicator}</div>",
#     unsafe_allow_html=True
# )
# Streamlit session state initialization
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input from the user
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send the prompt to the Google Generative AI model
    response = chat.send_message(prompt)

    # Display the response from the model
    with st.chat_message("assistant"):
        st.markdown(response.text)

    # Append the response to the session state
    st.session_state.messages.append({"role": "assistant", "content": response.text})
