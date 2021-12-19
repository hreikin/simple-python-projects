# Make a list of magician’s names. Pass the list to a function called 
# show_magicians() , which prints the name of each magician in the list.

names = ["Houdini", "Penn", "Teller"]

def show_magicians(list_of_names):
    for name in list_of_names:
        print("Magician:", name)

show_magicians(names)