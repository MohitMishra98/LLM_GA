import google.generativeai as genai
import os

from bs4 import BeautifulSoup
import requests

light_state = False

generation_config = {
  "temperature": 0,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

#always define the datatype of parameters
#and description of function in """ """
def scrape_webpage(url:str):
  """
  Scrapes the content of a webpage given its URL.

  Args:
    url: The URL of the webpage to scrape.

  Returns:
    The text content of the webpage.
  """
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  # Extract text content from the HTML
  page_content = soup.get_text(separator=' ', strip=True)
  return page_content

def turn_on_switch():
    """Turns off the light"""
    global light_state
    light_state = True
    return "turned on lights"

def turn_off_switch():
    """Turns ON the light"""
    global light_state
    light_state = False
    return "turn of lights"

def mul(a:int,b:int):
    """returns multiplication of 2 numbers a and b"""
    return a*b

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.0-pro",tools=[scrape_webpage,turn_on_switch,turn_off_switch,mul],generation_config=generation_config)
#define the tools in model object

chat = model.start_chat(history=[],enable_automatic_function_calling=True)

while True:
   user_input = input("Enter a prompt : ")
   response = chat.send_message(user_input)
   print(response.text)
   print(light_state)