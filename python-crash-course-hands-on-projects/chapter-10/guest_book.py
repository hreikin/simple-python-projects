# Write a while loop that prompts users for their name. When they enter their 
# name, print a greeting to the screen and add a line recording their visit in a 
# file called guest_book.txt. Make sure each entry appears on a new line in the 
# file.

filename = "python-crash-course-hands-on-projects/chapter-10/guest_book.txt"
running = True

while running:
    guest = input("Please input your name, press ENTER to exit: ")
    if guest == "":
        running = False
    else:
        print("Hello", guest)
        with open(filename, "a") as file_object:
            file_object.write(guest + "\n")