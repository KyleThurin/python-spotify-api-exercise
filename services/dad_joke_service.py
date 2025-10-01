import requests


def getDadJoke():
    url = "https://icanhazdadjoke.com" # Indexes the string for the website

    # Creates a dictionary
    headers = {
        "Accept": "application/json"
    }

    try:
        response    = requests.get(url, headers=headers)# Indexes the 'response'
        response.raise_for_status()                     # Provides error if something went wrong with 'request'
        joke_data   = response.json()                   # Indexes the joke
        #print(joke_data)
        return joke_data["joke"]                        # Returns 'joke'
    except requests.RequestException as e:
        print("Error getting joke: " + e)
        return None
