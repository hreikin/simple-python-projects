# Add an if test to the code from hello_admin.py to make sure the list of users 
# is not empty.
#
# If the list is empty, print the message We need to find some users!
# 
# Remove all of the usernames from your list, and make sure the correct message 
# is printed.

usernames = ["admin", "hreikin", "morgan", "jay", "neil"]

for name in usernames:
    if name == "admin":
        print(f"Hello {name}, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again.")

usernames = []

if usernames:
    for name in usernames:
        if name == "admin":
            print(f"Hello {name}, would you like to see a status report?")
        else:
            print(f"Hello {name}, thank you for logging in again.")
else:
    print("We need to find some user!")