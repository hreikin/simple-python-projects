# Make a list of people who should take the favorite languages poll. Include 
# some names that are already in the dictionary and some that are not.
# 
# Loop through the list of people who should take the poll. If they have already 
# taken the poll, print a message thanking them for responding. If they have not 
# yet taken the poll, print a message inviting them to take the poll.

favorite_languages = {
                    'jen': 'python',
                    'sarah': 'c',
                    'edward': 'ruby',
                    'phil': 'python',
                    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
    language.title() + ".")

poll_list = []

for k in favorite_languages.keys():
    if k == "jen" or k == "phil":
        poll_list.append(k)

poll_list.append("jay")
poll_list.append("neil")

print(poll_list)

for name in poll_list:
    if name in favorite_languages.keys():
        print(f"Thanks for taking the poll {name}.")
    else:
        print(f"{name} please take the poll.")