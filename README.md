# Spotify-Song-Game
A Spotify API Integrated Python Game

Hey there, music explorer! 🎶 Ready to test how well you know your friends' music vibes? Let's play "Who Likes This Song?" where you'll be a musical detective, guessing which friend jams to which song from their Spotify playlists. We'll sneak a peek into their public playlists, pick a random track, and your mission is to match the song to its fan. Guess right and feel like a music guru; guess wrong, and we'll let you in on who really digs that tune. Get set for a fun, tune-filled guessing game that's all about vibes, guesses, and good times! 🌟🎧

# Code Explanation

Authentication with Spotify: The script begins by obtaining an access token from Spotify using the provided client_id and client_secret. This token is necessary for making authenticated requests to the Spotify API.

User Playlists Retrieval: The script defines a list of user IDs (user_ids). For each user, it retrieves their playlists from Spotify. It filters these playlists to include only public ones, ensuring that the game uses accessible data.

Random Playlist and Track Selection: For each user, a random public playlist is chosen. From this playlist, a random track is selected. The track's name is then stored in a dictionary (user_playlists), keyed by the user's ID.

Gameplay Mechanism: After populating the user_playlists dictionary with a track for each user, the script randomly selects one entry (a user ID and their corresponding song name). It then prompts the player to guess which user likes the specified song.

User Input and Validation: The player inputs their guess as to which user is associated with the chosen song. The script checks this guess against the actual user ID and provides feedback, indicating whether the guess was correct or revealing the right answer if the guess was wrong.
