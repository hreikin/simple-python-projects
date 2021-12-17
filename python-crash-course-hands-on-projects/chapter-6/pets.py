# Make several dictionaries, where the name of each dictionary is the name of a 
# pet. In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets . Next, loop through your list 
# and as you do print everything you know about each pet.

rexy = {"type" : "dog", "owner" : "victoria"}
mush = {"type" : "dog", "owner" : "michael"}
pets = [rexy, mush]

for pet in pets:
    for k, v in pet.items():
        print(k + ":", v)