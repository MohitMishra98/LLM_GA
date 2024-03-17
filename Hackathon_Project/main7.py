import requests
from bs4 import BeautifulSoup
import re

def get_website_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.get_text()
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def search_websites(query, num_results=10):
    search_url = f"https://www.google.com/search?q={query}&num={num_results}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = []

    for result in soup.find_all('div', class_='yuRUbf'):
        link = result.find('a')['href']
        search_results.append(link)

    website_contents = []

    for url in search_results:
        content = get_website_content(url)
        if content:
            website_contents.append(content)

    return website_contents

# Example usage
search_query = 'Python programming'
website_contents = search_websites(search_query)

for i, content in enumerate(website_contents, start=1):
    print(f"Website {i} Content:")
    print(content[:500])  # Print the first 500 characters of each website's content
    print("---")