# Combine the two programs from "favourite_number_dump.py" and 
# "favourite_number_load.py" into one file. If the number is already stored, 
# report the favorite number to the user. If not, prompt for the user’s favorite 
# number and store it in a file. Run the program twice to see that it works.

import json

filename = "python-crash-course-hands-on-projects/chapter-10/favourite_numbers.json"

try:
    with open(filename, "r") as file_object:
        favourite_number = json.load(file_object)
except FileNotFoundError:
    favourite_number = input("What is your favourite number: ")
    with open(filename, "w") as file_object:
        json.dump(favourite_number, file_object)
else:
    print(f"I know your favourite number, it's {favourite_number}.")