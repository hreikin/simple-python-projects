# You just heard that one of your guests can’t make the dinner, so you need to 
# send out a new set of invitations. You’ll have to think of someone else to 
# invite. 
# 
# Start with your program from the previous exercise. Add a print statement at 
# the end of your program stating the name of the guest who can’t make it. 
# 
# Modify your list, replacing the name of the guest who can’t make it with the 
# name of the new person you are inviting. 
# 
# Print a second set of invitation messages, one for each person who is still in 
# your list.

print("Version 1:")
names = ["Morgan", "Jay", "Neil"]
message = "Would you like to come to dinner"
print(f"Would you like to come to dinner {names[0]}.")
print(f"Would you like to come to dinner {names[1]}.")
print(f"Would you like to come to dinner {names[2]}.")
print(f"{names[0]} can't make it.")
del names[0]
names.append("Gareth")
print(f"Would you like to come to dinner {names[0]}.")
print(f"Would you like to come to dinner {names[1]}.")
print(f"Would you like to come to dinner {names[2]}.")

print("Version 2:")
print(f"{message} {names[0]}.")
print(f"{message} {names[1]}.")
print(f"{message} {names[2]}.")
print(f"{names[0]} can't make it.")
del names[0]
names.append("Richard")
print(f"{message} {names[0]}.")
print(f"{message} {names[1]}.")
print(f"{message} {names[2]}.")

print("Version 3:")
for name in names:
    print(f"{message} {name}.")
print(f"{names[0]} can't make it.")
del names[0]
names.append("Alex")
for name in names:
    print(f"{message} {name}.")