# Generate random integer values
from random import seed
from random import randint

# Seed random number generator.
seed()

# Set number to be guessed and the "running" variable to True so the "while" loop keeps going until it is changed to False.
number = randint(1, 10)
running = True

# If the variable "running" is True keep going through the loop
while running:
    guess = int(input("Guess a number between 1 and 10: "))

    # If the guess is equal to the number print out the winning statement.
    if guess == number:
        print("Congratulations, that is correct!")

        # This causes the while loop to stop.
        running = False

    # If the guess is less than the number print out a statement advising them to guess higher.
    elif guess < number:
        print("No, it's a little higher than that.")

    # If neither of the above are true (so they guessed higher than the number) print out a statement advising them to guess lower.
    else:
        print("No, it's a little lower than that.")

# Once the "while" loop has completed print out the finished message.
else:
    print("Game completed.")

print("Goodbye.")