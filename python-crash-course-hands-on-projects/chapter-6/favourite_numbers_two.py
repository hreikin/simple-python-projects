# Modify your program from "favourite_numbers_one.py" so each person can have 
# more than one favorite number. Then print each person’s name along with their 
# favorite numbers.

favourite_numbers = {"gareth": [5, 6], "hreikin": [13, 14], "morgan": [20, 21], "jay": [7, 8], "neil": [32, 33]}

for name in favourite_numbers.keys():
    print(name)
    for number in favourite_numbers[name]:
        print(number)