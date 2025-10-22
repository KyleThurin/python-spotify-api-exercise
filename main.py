from services import dad_joke_service
from services import spotify_service

def main():
    print("Want to hear a joke?")
    joke = dad_joke_service.get_dad_joke()
    if joke:
        print(joke)
    print("-" * 20)

    token = spotify_service.get_token()
    # Error Handling for Token
    if not token:
        print("\nCould not retrieve Spotify access token. ")
        print("\nCheck your environment variables.")
        print("\nExiting.")
        return

    artist_name = input('Please enter the artist to search for: ')
    result      = spotify_service.search_for_artist(token, artist_name)
    # Error Handling for Artist Search
    if not result:
        print(f"No results found for '{artist_name}'.")
        print("\nExiting.")
        return

    artist_id = result["id"]
    tracks    = spotify_service.get_songs_by_artist(token, artist_id)

    if tracks:
        print(f"\nHere are the top 10 tracks for {result.get('name', 'the artist')}:")
        for idx, song in enumerate(tracks):
            print(f"{idx + 1}. {song['name']}")
    else:
        print("\nNo tracks found for this artist.")



if __name__ == "__main__":
    main()