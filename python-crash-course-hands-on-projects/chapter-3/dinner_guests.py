# Working with one of the programs from a previous exercise, use len() to print 
# a message indicating the number of people you are inviting to dinner.
#
#
# Taken from "more-guests.py".

names_c = ["Morgan", "Jay", "Neil"]
message = "Would you like to come to dinner"

def version_c():
    print("Version C")
    for name in names_c:
        print(f"{message} {name}.")
    print(f"{names_c[0]} can't make it.")
    del names_c[0]
    names_c.append("Gareth")
    for name in names_c:
        print(f"{message} {name}.")
    print("We found a bigger table, let's invite some more people.")
    names_c.insert(0, "Morgan")
    names_c.insert(2, "Richard")
    names_c.append("Alex")
    for name in names_c:
        print(f"{message} {name}.")
    guests = len(names_c)
    print(f"There will be {guests} people coming to dinner.")

version_c()