# If you could invite anyone, living or deceased, to dinner, who would you 
# invite? Make a list that includes at least three people you’d like to invite 
# to dinner. Then use your list to print a message to each person, inviting them 
# to dinner.

names = ["Morgan", "Jay", "Neil"]
message = "Would you like to come to dinner"
print(f"Would you like to come to dinner {names[0]}.")
print(f"Would you like to come to dinner {names[1]}.")
print(f"Would you like to come to dinner {names[2]}.")

print(f"{message} {names[0]}.")
print(f"{message} {names[1]}.")
print(f"{message} {names[2]}.")

for name in names:
    print(f"Would you like to come to dinner {name}.")