# A movie theater charges different ticket prices depending on a person’s age. 
# If a person is under the age of 3, the ticket is free; if they are between 3 
# and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
# Write a loop in which you ask users their age, and then tell them the cost of 
# their movie ticket.

answer = ""

while answer != "quit":
    answer = input("How old are you ? To exit type 'quit'. ")
    if answer == "quit":
        print("Ok, quitting.")
        break
    elif int(answer) < 3:
        print("Your ticket is free.")
    elif int(answer) >= 3 and int(answer) <= 12:
        print("Your ticket is £10 please.")
    elif int(answer) > 12:
        print("Your ticket is £15 please.")