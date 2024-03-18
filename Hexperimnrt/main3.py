import google.generativeai as genai
import os

from bs4 import BeautifulSoup
import requests

light_state = "False"

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

def lightSwitch(state: str):
    """Turns on the light when ON And Turns off the light when OFF
    
      Args:
    state: state of the light ON or OFF

  Returns:
    The text content of the webpage."""
    light_state = state

    return "Changed the state of light"

def mul(a:int,b:int):
    """returns multiplication of 2 numbers a and b"""
    return a*b

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.0-pro",tools=[scrape_webpage,lightSwitch,mul])
#define the tools in model object

chat = model.start_chat(enable_automatic_function_calling=True)

messages = [{"role":"user","parts":["user message1"]},
            {"role":"model","parts":["model message1"]},
            {"role":"user","parts":["user message2"]},
            {"role":"model","parts":["user message2"]},]
#specifically use this structre otherwise it will not work

messages = []

while True:
    #taking input from user
    new_prompt = input()
    if(new_prompt=="AAAA"):
        break
    #adding user message of the conversation list
    messages.append({"role":"user","parts":[new_prompt]})
    #generating model response by provideing list
    response = model.generate_content(messages)
    #adding model message of the conversation list
    messages.append({"role":"model","parts":[response.text]})
    #printing response to the user
    print(response.text)
    print(light_state)


print(messages)

#works perfectly
print("this is for loop")
for i in messages:
    print(f"{i["role"]} : {i["parts"][0]}")