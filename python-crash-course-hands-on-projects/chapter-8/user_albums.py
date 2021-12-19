# Start with your program from "albums.py". Write a while loop that allows users 
# to enter an album’s artist and title. Once you have that information, call 
# make_album() with the user’s input and print the dictionary that’s created. 
# Be sure to include a quit value in the while loop.

def make_album(artist, album, tracks = 0):
    album_dict = {"Artist" : artist, "Album" : album}
    if tracks:
        album_dict["Tracks"] = tracks
    return album_dict

while True:
    artist = input("Enter an artist, type 'quit' to exit: ")
    if artist == "quit":
        print("Ok, quitting.")
        break
    album = input("Enter an album name, type 'quit' to exit: ")
    if album == "quit":
        print("Ok, quitting.")
        break
    output = make_album(artist, album)
    for k, v in output.items():
        print(k + ":", v)