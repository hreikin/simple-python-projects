# Write a while loop that asks people why they like programming. Each time 
# someone enters a reason, add their reason to a file that stores all the 
# responses.

filename = "python-crash-course-hands-on-projects/chapter-10/programming_poll.txt"
running = True

while running:
    response = input("Please enter a reason why you like programming, just hit ENTER to quit: ")
    if response == "":
        running = False
    else:
        with open(filename, "a") as file_object:
            file_object.write(response + "\n")