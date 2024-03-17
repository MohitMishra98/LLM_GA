import requests
from bs4 import BeautifulSoup
from googlesearch import search

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
    search_results = search(query, num=num_results)
    website_contents = []

    for url in search_results:
        content = get_website_content(url)
        if content:
            website_contents.append(content)

    return website_contents

# Example usage
search_query = 'AI nEWS'
website_contents = search_websites(search_query)

for i, content in enumerate(website_contents, start=1):
    print(f"Website {i} Content:")
    print(content)
    print("---")