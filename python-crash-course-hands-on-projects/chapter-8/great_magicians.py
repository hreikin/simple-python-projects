# Start with a copy of your program from "magicians.py". Write a function called 
# make_great() that modifies the list of magicians by adding the phrase the 
# Great to each magician’s name. Call show_magicians() to see that the list has 
# actually been modified.

def show_magicians(list_of_names):
    for name in list_of_names:
        print(name)

def make_great(list_of_names):
    great_names = []

    while list_of_names:
        name = list_of_names.pop()
        great_name = name + " the great"
        great_names.append(great_name)

    for name in great_names:
        list_of_names.append(name)


magicians = ["Houdini", "Penn", "Teller"]
show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)