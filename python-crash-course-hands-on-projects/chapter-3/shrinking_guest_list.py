# You just found out that your new dinner table won’t arrive in time for the 
# dinner, and you have space for only two guests. 
# 
# Start with your program from the previous exercise. Add a new line that prints 
# a message saying that you can invite only two people for dinner. 
# 
# Use pop() to remove guests from your list one at a time until only two names 
# remain in your list. Each time you pop a name from your list, print a message 
# to that person letting them know you’re sorry you can’t invite them to dinner. 
# 
# Print a message to each of the two people still on your list, letting them 
# know they’re still invited. 
# 
# Use del to remove the last two names from your list, so you have an empty list. 
# Print your list to make sure you actually have an empty list at the end of 
# your program.

names_a = ["Morgan", "Jay", "Neil"]
names_b = ["Morgan", "Jay", "Neil"]
names_c = ["Morgan", "Jay", "Neil"]
message = "Would you like to come to dinner"
apology = "Sorry you can't come now"
confirmation = "You are still coming to dinner"

def version_a():
    print("Version A")
    print(f"Would you like to come to dinner {names_a[0]}.")
    print(f"Would you like to come to dinner {names_a[1]}.")
    print(f"Would you like to come to dinner {names_a[2]}.")
    print(f"{names_a[0]} can't make it.")
    del names_a[0]
    names_a.append("Gareth")
    print(f"Would you like to come to dinner {names_a[0]}.")
    print(f"Would you like to come to dinner {names_a[1]}.")
    print(f"Would you like to come to dinner {names_a[2]}.")
    print("We found a bigger table, let's invite some more people.")
    names_a.insert(0, "Morgan")
    names_a.insert(2, "Richard")
    names_a.append("Alex")
    print(f"Would you like to come to dinner {names_a[0]}.")
    print(f"Would you like to come to dinner {names_a[1]}.")
    print(f"Would you like to come to dinner {names_a[2]}.")
    print(f"Would you like to come to dinner {names_a[3]}.")
    print(f"Would you like to come to dinner {names_a[4]}.")
    print(f"Would you like to come to dinner {names_a[5]}.")
    print("I can now only invite 2 people.")
    popped_name = names_a.pop()
    print(f"Sorry you can't come now {popped_name}.")
    popped_name = names_a.pop()
    print(f"Sorry you can't come now {popped_name}.")
    popped_name = names_a.pop()
    print(f"Sorry you can't come now {popped_name}.")
    popped_name = names_a.pop()
    print(f"Sorry you can't come now {popped_name}.")
    print(f"You are still coming to dinner {names_a[0]}")
    print(f"You are still coming to dinner {names_a[1]}")
    print("I will now delete the last 2 names.")
    del names_a[0:2]
    print(f"The list is now empty: {names_a}")

def version_b():
    print("Version B")
    print(f"{message} {names_b[0]}.")
    print(f"{message} {names_b[1]}.")
    print(f"{message} {names_b[2]}.")
    print(f"{names_b[0]} can't make it.")
    del names_b[0]
    names_b.append("Gareth")
    print(f"{message} {names_b[0]}.")
    print(f"{message} {names_b[1]}.")
    print(f"{message} {names_b[2]}.")
    print("We found a bigger table, let's invite some more people.")
    names_b.insert(0, "Morgan")
    names_b.insert(2, "Richard")
    names_b.append("Alex")
    print(f"{message} {names_b[0]}.")
    print(f"{message} {names_b[1]}.")
    print(f"{message} {names_b[2]}.")
    print(f"{message} {names_b[3]}.")
    print(f"{message} {names_b[4]}.")
    print(f"{message} {names_b[5]}.")
    print("I can now only invite 2 people.")
    popped_name = names_b.pop()
    print(f"{apology} {popped_name}.")
    popped_name = names_b.pop()
    print(f"{apology} {popped_name}.")
    popped_name = names_b.pop()
    print(f"{apology} {popped_name}.")
    popped_name = names_b.pop()
    print(f"{apology} {popped_name}.")
    print(f"{confirmation} {names_b[0]}")
    print(f"{confirmation} {names_b[1]}")
    print("I will now delete the last 2 names.")
    del names_b[0:2]
    print(f"The list is now empty: {names_b}")

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
    print("I can now only invite 2 people.")
    for name in names_c[:-2]:
        popped_name = names_c.pop()
        print(f"{apology} {popped_name}.")
    for name in names_c:
        print(f"{confirmation} {name}.")
    print("I will now delete the last 2 names.")
    del names_c[0:2]
    print(f"The list is now empty: {names_c}")

version_a()
version_b()
version_c()