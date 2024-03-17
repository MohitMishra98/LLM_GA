import requests
from bs4 import BeautifulSoup

# Set up the Serper API endpoint and your API key
api_endpoint = "https://google.serper.dev/search"
api_key = "4f51317c2911c9b495988832f4d0c4c1e9ebd27f"  # Replace with your valid API key

# Prompt the user for the search query
query = input("Enter your search query: ")

# Set up the API request parameters
params = {
    "q": query,
    "num": 5,  # Retrieve the top 5 results
    "api_key": api_key
}

try:
    # Send the API request
    response = requests.get(api_endpoint, params=params)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful

    # Parse the JSON response
    data = response.json()

    # Extract the content of the top 5 results
    for i, result in enumerate(data["organic"], start=1):
        print(f"Result {i}:")
        print("Title:", result["title"])
        print("URL:", result["link"])

        # Fetch the webpage content
        webpage_response = requests.get(result["link"])
        webpage_response.raise_for_status()  # Raise an exception if the request was unsuccessful

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(webpage_response.text, "html.parser")

        # Extract the desired information from the webpage (e.g., the main content)
        main_content = soup.find("div", class_="main-content")
        if main_content:
            print("Main Content:")
            print(main_content.get_text())
        else:
            print("Main content not found.")

        print()

except requests.exceptions.RequestException as e:
    print("An error occurred while making the API request or fetching the webpage:", e)
    print("Please check your API key, ensure you have the necessary permissions, and verify the webpage URL.")

except (KeyError, IndexError) as e:
    print("An error occurred while parsing the API response or webpage content:", e)