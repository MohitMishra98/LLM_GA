import requests

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
        print("Snippet:", result["snippet"])
        print()

except requests.exceptions.RequestException as e:
    print("An error occurred while making the API request:", e)
    print("Please check your API key and ensure you have the necessary permissions.")
except (KeyError, IndexError) as e:
    print("An error occurred while parsing the API response:", e)
