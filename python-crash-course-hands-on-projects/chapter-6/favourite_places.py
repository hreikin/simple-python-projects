# Make a dictionary called favorite_places. Think of three names to use as keys 
# in the dictionary, and store one to three favorite places for each person. To 
# make this exercise a bit more interesting, ask some friends to name a few of 
# their favorite places. Loop through the dictionary, and print each person’s 
# name and their favorite places.

favourite_places = {"jay" : ["france", "spain", "germany"], "neil" : ["scotland", "wales", "ireland"], "morgan" : ["england", "holland", "belgium"]}

for name in favourite_places.keys():
    print("name: " + name)
    print("favourite places:")
    for place in favourite_places[name]:
        print(place)