from dotenv import load_dotenv
import requests
import base64
import os

'''
For Spotify API info, visit: https://developer.spotify.com/documentation/web-api/tutorials/client-credentials-flow
'''

load_dotenv()

client_id       = os.getenv("SPOTIFY_CLIENT_ID")
client_secret   = os.getenv("SPOTIFY_CLIENT_SECRET")
#print(client_id, client_secret)

# UPDATE: The index URLs are now constants
SPOTIFY_AUTH_URL    = "https://accounts.spotify.com/api/token"
SPOTIFY_SEARCH_URL  = "https://api.spotify.com/v1/search"
SPOTIFY_TRACKS_BASE = "https://api.spotify.com/v1/artists/" # Base for /artists/{id}/top-tracks




def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes  = auth_string.encode("utf-8")
    auth_base64 = str( base64.b64encode(auth_bytes), 'utf-8')
    #url         = "https://accounts.spotify.com/api/token"
    url = SPOTIFY_AUTH_URL

    # Creates dictionaries
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data    = {'grant_type': 'client_credentials'}

    try:
        results = requests.post(url,
                                headers=headers,
                                data=data)
        # Provides error response if something went wrong with 'request'
        results.raise_for_status()
        data    = results.json()
        token   = data["access_token"]
        return token
    except requests.HTTPError as http_err:
        print(f'HTTP Error occurred: {http_err}')
        print('\nPlease make sure the "SPOTIFY_CLIENT_ID" and "SPOTIFY_CLIENT_SECRET" are correct in the .env file')
    except requests.RequestException as ex:
        print(f'\nException occurred during token retrieval: {ex}')
        return None

def get_auth_header(token):
    return { "Authorization": "Bearer " + token }

def search_for_artist(token, artist_name):
    #url         = "https://api.spotify.com/v1/search"       # Indexes URL string (endpoint)
    #url = SPOTIFY_SEARCH_URL
    #query       = f"?q={artist_name}&limit=1&type=artist"
    #query_url   = url + query
    query_url = SPOTIFY_SEARCH_URL + f"?q={artist_name}&limit=1&type=artist"
    #headers     = { "Authorization": "Bearer " + token }
    headers     = get_auth_header(token)

    try:
        result  = requests.get(query_url, headers=headers)
        data    = result.json()
        items   = data['artists']['items']
        if items:
            return items[0]
        else:
            print(f"Artist '{artist_name}' not found.")
            return None
    except Exception as e:
        print(f"Unexpected error during artist search: {e}")


def get_songs_by_artist(token, artist_id):
    #url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US" # Indexes URL string
    url     = f"{SPOTIFY_TRACKS_BASE}{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result  = requests.get(url, headers=headers)
    data    = result.json()
    return data["tracks"]


