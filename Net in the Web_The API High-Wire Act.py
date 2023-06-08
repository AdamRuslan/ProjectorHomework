import requests

def search_gifs(search_term, api_key):
    url = f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={search_term}&limit=5"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        for gif in data["data"]:
            gif_url = gif["images"]["original"]["url"]
            print(gif_url)
            
    except requests.exceptions.HTTPError as error:
        print(f"An HTTP error occurred: {error}")
    except requests.exceptions.RequestException as error:
        print(f"An error occurred: {error}")

# Replace "YOUR_API_KEY" with your actual Giphy API key
api_key = "zskeAiq9VsWRrdkayweeOAFiYnx3iKiK"
search_term = input("Enter a search term: ")

search_gifs(search_term, api_key)
