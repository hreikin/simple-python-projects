# Write a program that prompts for the user’s favorite number. Use json.dump() 
# to store this number in a file. Write a separate program that reads in this 
# value and prints the message, “I know your favorite number! It’s _____.”

import json

filename = "python-crash-course-hands-on-projects/chapter-10/favourite_numbers.json"

with open(filename, "r") as file_object:
    favourite_number = json.load(file_object)
print(f"I know your favourite number, it's {favourite_number}.")