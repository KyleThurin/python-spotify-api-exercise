
from services import dad_joke_service
from services import spotify_service

def main():
    print("Want to hear a joke?")
    joke = dad_joke_service.getDadJoke()# Indexes a dad joke
    print(joke)                         # Displays the joke

    token       = spotify_service.get_token()                           # Indexes the token
    artist_name = input('Enter the artist to search for: ')             # Indexes the user input
    result      = spotify_service.search_for_artist(token, artist_name) # Searches for the artest using the user input
    artist_id   = result["id"]                                          # Indexes the 'id' of the result

    tracks      = spotify_service.get_songs_by_artist(token, artist_id) # Searches for the songs for the artest

    # Loops through 'tracks'
    for idx, song in enumerate(tracks):
        # Displays the current 'song' and index value
        print (f"{idx + 1}. {song['name']}")


if __name__ == "__main__":
    main()