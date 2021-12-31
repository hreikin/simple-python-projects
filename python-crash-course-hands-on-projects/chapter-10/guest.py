# Write a program that prompts the user for their name. When they respond, write 
# their name to a file called guest.txt.

filename = "python-crash-course-hands-on-projects/chapter-10/guest.txt"
guest = input("Please input your name: ")

with open(filename, "w") as file_object:
    file_object.write(guest)