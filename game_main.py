import requests
import json
import random

client_id = "1759317b7907431396fcaf64cf6672f4"
client_secret = "0428d3fc93554fbebe8add9f5677499a"


def get_access_token():
    """
    Function to retrieve access token using client ID and client secret
    """
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    response = requests.post('https://accounts.spotify.com/api/token', data=data)
    response.raise_for_status()

    data = response.json()
    access_token = data['access_token']
    return access_token


def get_user_playlists(access_token, user_ids):
    """
    Function to get a random playlist and track for each user
    """
    user_playlists = {}

    for user_id in user_ids:
        try:
            headers = {
                'Authorization': 'Bearer ' + access_token
            }

            response = requests.get('https://api.spotify.com/v1/users/' + user_id + '/playlists', headers=headers)
            response.raise_for_status()

            playlists = response.json()['items']

            public_playlists = [playlist for playlist in playlists if playlist['public']]

            if not public_playlists:
                print(f"No public playlists found for user {user_id}. Skipping...")
                continue

            selected_playlist = public_playlists[random.randint(0, len(public_playlists) - 1)]

            response = requests.get('https://api.spotify.com/v1/playlists/' + selected_playlist['id'] + '/tracks', headers=headers)
            response.raise_for_status()

            tracks = response.json()['items']

            selected_track = random.choice(tracks)

            user_playlists[user_id] = selected_track['track']['name']
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"User {user_id} not found")
            else:
                raise e

    return user_playlists


def add_friends():
    """
    Function to add user IDs from user input
    """
    answer = input("Would you like to add your own friends' user IDs? (yes/no): ")
    if answer.lower() == "yes":
        new_user_ids = []
        for i in range(4):
            user_id = input(f"Enter user ID {i + 1}: ")
            new_user_ids.append(user_id)
        return new_user_ids
    elif answer.lower() == "no":
        return ["Idachen", "helenestrobl", "josi.elmahdy","strobl.toni"]
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return add_friends()


def main():
    access_token = get_access_token()
    user_ids = add_friends()
    user_playlists = get_user_playlists(access_token, user_ids)

    user_id, song_name = random.choice(list(user_playlists.items()))

    guess = input(f"Which user likes this song: {song_name}? ")

    if guess == user_id:
        print("Correct!")
    else:
        print("Wrong! It is:", user_id)


if __name__ == "__main__":
    main()
