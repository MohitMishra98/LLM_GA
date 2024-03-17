import requests

# Set up the Serper API endpoint and your API key
api_endpoint = "https://google.serper.dev/search"
api_key = "4f51317c2911c9b495988832f4d0c4c1e9ebd27f"

# Prompt the user for the website URL
url = input("Enter the website URL: ")

# Set up the API request parameters
params = {
    "url": url,
    "api_key": api_key
}

try:
    # Send the API request
    response = requests.get(api_endpoint, params=params)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful

    # Parse the JSON response
    data = response.json()

    # Extract the full content of the website
    content = data["content"]

    print("Website Content:")
    print(content)

except requests.exceptions.RequestException as e:
    print("An error occurred while making the API request:", e)
except (KeyError, IndexError) as e:
    print("An error occurred while parsing the API response:", e)