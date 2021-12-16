# Do the following to create a program that simulates how websites ensure that 
# everyone has a unique username.
# 
# Make a list of five or more usernames called current_users .
# 
# Make another list of five usernames called new_users . Make sure one or two of 
# the new usernames are also in the current_users list.
# 
# Loop through the new_users list to see if each new username has already been 
# used. If it has, print a message that the person will need to enter a new 
# username. If a username has not been used, print a message saying that the 
# username is available.
# 
# Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' 
# should not be accepted.

current_users = ["admin", "hreikin", "morgan", "jay", "neil"]
new_users = ["Admin", "mark", "Hreikin", "danny", "dave"]

for name in new_users:
    if name.lower() in current_users:
        print(f"The username {name} is taken, please choose another.")
    else:
        print(f"The username {name} is available.")