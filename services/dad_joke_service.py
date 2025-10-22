import requests

# UPDATE: The index URL is now constant
DAD_JOKE_URL = "https://icanhazdadjoke.com"

def get_dad_joke():
    #url = "https://icanhazdadjoke.com" # Indexes the string for the website
    url = DAD_JOKE_URL

    # Creates a dictionary
    headers = {
        "Accept": "application/json"
    }

    try:
        response    = requests.get(url, headers=headers)
        # Provides error response if something went wrong with 'request'
        response.raise_for_status()
        joke_data   = response.json()
        return joke_data["joke"]
    except requests.RequestException as e:
        print(f"\nError getting joke: {e}")
        return None
