# Write a loop that prompts the user to enter a series of pizza toppings until 
# they enter a 'quit' value. As they enter each topping, print a message saying 
# you’ll add that topping to their pizza.

question = "What topping do you want? To exit type 'quit': "

while True:
    answer = input(question)
    if answer == "quit":
        print("Ok, quitting.")
        break
    else:
        print("Ok, adding it to your pizza.")