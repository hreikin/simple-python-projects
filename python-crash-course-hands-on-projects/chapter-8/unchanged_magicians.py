# Start with your work from "great_magicians.py". Call the function make_great() 
# with a copy of the list of magicians’ names. Because the original list will be 
# unchanged, return the new list and store it in a separate list. Call 
# show_magicians() with each list to show that you have one list of the original 
# names and one list with the Great added to each magician’s name.

def show_magicians(list_of_names):
    for name in list_of_names:
        print(name)

def make_great(list_of_names):
    great_names = []

    while list_of_names:
        name = list_of_names.pop()
        great_name = name + " the great"
        great_names.append(great_name)

    for great_name in great_names:
        list_of_names.append(great_name)
    
    return list_of_names


magicians = ["Houdini", "Penn", "Teller"]
show_magicians(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal magicians:")
show_magicians(magicians)