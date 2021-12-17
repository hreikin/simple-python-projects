# Use a dictionary to store people’s favorite numbers. Think of five names, and 
# use them as keys in your dictionary. Think of a favorite number for each 
# person, and store each as a value in your dictionary. Print each person’s name 
# and their favorite number. For even more fun, poll a few friends and get some 
# actual data for your program.

favourite_numbers = {"gareth": 5, "hreikin": 13, "morgan": 20, "jay": 7, "neil": 32}

for k, v in favourite_numbers.items():
    print(k + ":", v)