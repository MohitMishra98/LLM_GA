import google.generativeai as genai
import os

from bs4 import BeautifulSoup
import requests


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

# # Example usage
# url = "https://ai.google.dev/tutorials/function_calling_python_quickstart"
# content = scrape_webpage(url)
# print(content)

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.0-pro",tools=[scrape_webpage])
#define the tools in model object

chat = model.start_chat(enable_automatic_function_calling=True)

response = chat.send_message("summarize contents of this url https://ai.google.dev/tutorials/function_calling_python_quickstart ")

print(response.text)

#uncomment this
# for content in chat.history:
#     part = content.parts[0]
#     print(content.role, "->", type(part).to_dict(part))
#     print('-'*80)

