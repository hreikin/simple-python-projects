# Write a program that prompts for the user’s favorite number. Use json.dump() 
# to store this number in a file. Write a separate program that reads in this 
# value and prints the message, “I know your favorite number! It’s _____.”

import json

filename = "python-crash-course-hands-on-projects/chapter-10/favourite_numbers.json"

favourite_number = input("What is your favourite number: ")
with open(filename, "w") as file_object:
    json.dump(favourite_number, file_object)