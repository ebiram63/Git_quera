all_users = {}
all_albums = {}

def add_user(username: str, age: int, city: str, albums: list, all_users: dict, all_albums: dict):
        # Add user details to all_users dictionary
        all_users[username] = {
            'age': age,
            'city': city
        }
        
        # Add user albums to all_albums dictionary
        if albums:
            all_albums[username] = list(albums)
        else:
            all_albums[username] = []
        
        return all_users, all_albums

def add_album(album_name: str, artist_name: str, genre: str, tracks: list, all_users: dict, all_albums: dict):
    album_name =album_name
    album_info = {
            'album_name': album_name,
            'artist_name': artist_name,
            'genre': genre,
            'tracks': tracks
        }
    for v in all_albums.values():
        for d in v:
            if d == album_name:
                d = [album_info]
                
    return all_albums

def query_user_artist(username: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    # Check user
    if username not in all_users:
        raise ValueError(f"User '{username}' not found.")  
    # Check if the user has albums in the all_albums dictionary
    if username not in all_albums:
        return 0
    # Count the albums by the specified artist for the given user
    artist_album_count = 0
    for album in all_albums[username]:
        if album[artist_name] == artist_name:
            artist_album_count += sum(all_albums[tracks])
    
    return artist_album_count

def query_user_genre(username: str, genre: str, all_users: dict, all_albums: dict) -> int:
    # Check user
    if username not in all_users:
        raise ValueError(f"User '{username}' not found.")
    
    # Check if the user has albums in the all_albums dictionary
    if username not in all_albums:
        return 0
    
    # Count the albums of the specified genre for the given user
    genre_album_count = 0
    for album in all_albums[username]:
        if album == genre:
            genre_album_count += 1
    
    return genre_album_count

#-----

def query_age_artist(age: int, artist_name: str, all_users: dict, all_albums: dict) -> int:

    song_count = 0

    for username, user_info in all_users.items():
        if user_info['age'] == age:
            if username in all_albums:
                for album in all_albums[username]:
                    if album['artist_name'] == artist_name:
                        song_count += len(album['tracks'])

    return song_count

#-----
def query_age_genre(age: int, genre: str, all_users: dict, all_albums: dict) -> int:
    # Count the albums of the specified genre for users of the given age
    genre_album_count = 0

    # Loop through each user in all_users
    for username, user_info in all_users.items():
        # Check if the user's age matches the specified age
        if user_info['age'] == age:
            # Check if the user has albums in the all_albums dictionary
            if username in all_albums:
                # Count the albums of the specified genre for this user
                for album in all_albums[username]:
                    if album['genre'] == genre:
                        genre_album_count += 1

    return genre_album_count


def query_city_artist(city: str, artist_name: str, all_users: dict, all_albums: dict) -> int:
    # Count the albums by the specified artist for users from the given city
    artist_album_count = 0

    # Loop through each user in all_users
    for username, user_info in all_users.items():
        # Check if the user's city matches the specified city
        if user_info['city'] == city:
            # Check if the user has albums in the all_albums dictionary
            if username in all_albums:
                # Count the albums by the specified artist for this user
                for album in all_albums[username]:
                    if album['artist_name'] == artist_name:
                        artist_album_count += 1

    return artist_album_count


def query_city_genre(city: str, genre: str, all_users: dict, all_albums: dict) -> int:
    # Count the albums of the specified genre for users from the given city
    genre_album_count = 0

    # Loop through each user in all_users
    for username, user_info in all_users.items():
        # Check if the user's city matches the specified city
        if user_info['city'] == city:
            # Check if the user has albums in the all_albums dictionary
            if username in all_albums:
                # Count the albums of the specified genre for this user
                for album in all_albums[username]:
                    if album['genre'] == genre:
                        genre_album_count += 1

    return genre_album_count

# DO NOT USE YOUR OWN TESTS HERE, USE SAMPLE TEST INSTEAD
add_user("SAliB", 19, "Tehran", ["tekunbede", "barf", "gavazn"], all_users, all_albums)
print(add_user("Saeid", 22, "Esfehan", ["eclipse", "barf", "gavazn"], all_users, all_albums))
print(add_album("eclipse", "malmsteen", "classic", 10, all_users, all_albums))
print(add_album("barf", "beeptunes", "pop", 22, all_users, all_albums))
"""add_album("tekunbede", "beeptunes", "pop", 14, all_users, all_albums)
add_album("gavazn", "sorena", "persian", 18, all_users, all_albums)
add_user("Ali", 12, "Bushehr", ["bidad", "blaze"], all_users, all_albums)
add_album("bidad", "shajarian", "classic", 10, all_users, all_albums)
add_album("blaze", "ghorbani", "pop", 9, all_users, all_albums)
query_user_artist("Ali", "ghorbani", all_users, all_albums)
query_user_genre("Ali", "classic", all_users, all_albums)
query_age_artist(12, "shajarian", all_users, all_albums)
query_age_genre(12, "pop", all_users, all_albums)
query_city_artist("Bushehr", "ghorbani", all_users, all_albums)
query_city_genre("Bushehr", "pop", all_users, all_albums)"""

