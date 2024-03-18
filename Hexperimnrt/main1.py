import streamlit as st
import google.generativeai as genai
import os
from bs4 import BeautifulSoup
import requests

# Define the web scraping function
def scrape_webpage(url: str):
    """Scrapes the content of a webpage given its URL."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    page_content = soup.get_text(separator=' ', strip=True)
    return page_content

def lightSwitch(state: bool):
    """Turns on the light when True And Turns off the light when False"""
    light_state = state

# Set up Google Generative AI
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.0-pro", tools=[scrape_webpage,lightSwitch])

# Streamlit app
st.title("Web Content Summarizer")

url = st.text_input("Enter URL:")

while url:
    # Scrape the webpage content
    page_content = scrape_webpage(url)

    # Summarize the content using Generative AI
    chat = model.start_chat(enable_automatic_function_calling=True)
    response = chat.send_message(f"Summarize the contents of this URL: {url}")
    summary = response.text

    # Display the summary
    st.write("Summary:")
    st.write(summary)