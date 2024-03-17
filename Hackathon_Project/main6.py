from serpapi import GoogleSearch

def get_search_summaries(query, num_results=10):
    params = {
        "engine": "google",
        "q": query,
        "num": num_results,
        "api_key": "4f51317c2911c9b495988832f4d0c4c1e9ebd27f"  # Replace with your SerpApi API key
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    summaries = []
    for result in results.get("organic_results", []):
        summary = result.get("snippet")
        if summary:
            summaries.append(summary)

    return summaries

if __name__ == "__main__":
    query = "Python web scraping"
    summaries = get_search_summaries(query)

    for summary in summaries:
        print(summary)
        print("-" * 30)