import google.generativeai as genai
import os

from bs4 import BeautifulSoup
import requests

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

# Example usage
url = "https://indianexpress.com/article/explained/ai-elections-disinformation-9216941/"
content = scrape_webpage(url)
print(content)