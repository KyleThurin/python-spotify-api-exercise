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
        response    = requests.get(url, headers=headers)# Indexes the 'response'
        response.raise_for_status()                     # Provides error if something went wrong with 'request'
        joke_data   = response.json()                   # Indexes the joke
        return joke_data["joke"]                        # Returns 'joke'
    except requests.RequestException as e:
        print(f"Error getting joke: {e}")
        return None
