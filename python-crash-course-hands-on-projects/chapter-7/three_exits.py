# Write different versions of either "movie_tickets.py" or "pizza_toppings.py" 
# that do each of the following at least once:
# 
# Use a conditional test in the while statement to stop the loop.
# 
# Use an active variable to control how long the loop runs.
# 
# Use a break statement to exit the loop when the user enters a 'quit' value.

answer = ""

while answer != "quit":
    answer = input("How old are you ? To exit type 'quit': ")
    if answer == "quit":
        print("Ok, quitting.")
        break
    elif int(answer) < 3:
        print("Your ticket is free.")
    elif int(answer) >= 3 and int(answer) <= 12:
        print("Your ticket is £10 please.")
    elif int(answer) > 12:
        print("Your ticket is £15 please.")

question = "How old are you ? To exit type 'quit': "

while True:
    answer = input(question)
    if answer == "quit":
        print("Ok, quitting.")
        break
    elif int(answer) < 3:
        print("Your ticket is free.")
    elif int(answer) >= 3 and int(answer) <= 12:
        print("Your ticket is £10 please.")
    elif int(answer) > 12:
        print("Your ticket is £15 please.")

active = True

while active:
        answer = input(question)
        if answer == "quit":
            print("Ok, quitting.")
            active = False
        elif int(answer) < 3:
            print("Your ticket is free.")
        elif int(answer) >= 3 and int(answer) <= 12:
            print("Your ticket is £10 please.")
        elif int(answer) > 12:
            print("Your ticket is £15 please.")
