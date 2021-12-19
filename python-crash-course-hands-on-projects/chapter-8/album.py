# Write a function called make_album() that builds a dictionary describing a 
# music album. The function should take in an artist name and an album title, 
# and it should return a dictionary containing these two pieces of information. 
# 
# Use the function to make three dictionaries representing different albums. 
# Print each return value to show that the dictionaries are storing the album 
# information correctly. 
# 
# Add an optional parameter to make_album() that allows you to store the number 
# of tracks on an album. If the calling line includes a value for the number of 
# tracks, add that value to the album’s dictionary. Make at least one new 
# function call that includes the number of tracks on an album.

def make_album(artist, album, tracks = 0):
    album_dict = {"Artist" : artist, "Album" : album}
    if tracks:
        album_dict["Tracks"] = tracks
    return album_dict

album = make_album('metallica', 'ride the lightning')
for k, v in album.items():
    print(k + ":", v)

album = make_album('beethoven', 'ninth symphony')
for k, v in album.items():
    print(k + ":", v)

album = make_album('willie nelson', 'red-headed stranger')
for k, v in album.items():
    print(k + ":", v)

album = make_album('iron maiden', 'piece of mind', tracks = 8)
for k, v in album.items():
    print(k + ":", v)