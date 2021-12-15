# You just found a bigger dinner table, so now more space is available. Think of
# three more guests to invite to dinner. 
# 
# Start with your program from the previous exercise. Add a print statement to 
# the end of your program informing people that you found a bigger dinner table. 
# 
# Use insert() to add one new guest to the beginning of your list. 
# 
# Use insert() to add one new guest to the middle of your list. 
# 
# Use append() to add one new guest to the end of your list. 
# 
# Print a new set of invitation messages, one for each person in your list.

names_a = ["Morgan", "Jay", "Neil"]
names_b = ["Morgan", "Jay", "Neil"]
names_c = ["Morgan", "Jay", "Neil"]
message = "Would you like to come to dinner"

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

version_a()
version_b()
version_c()