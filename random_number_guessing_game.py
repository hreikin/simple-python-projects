# Generate random integer values
from random import seed
from random import randint

# Seed random number generator.
seed()

# Set number to be guessed and the "running" variable to True so the "while" loop keeps going until it is changed to False.
number = randint(1, 10)
running = True

current_try = 1
max_tries = 3

# Explain the game.
print("A number between 1 and 10 has been picked at random, can you guess which one it is ? You have 3 tries.")

# If the variable "running" is True keep going through the loop
while running:

    # Check if current_try is lower than max_tries. If it is then run through the loop, if it isn't then print "Game Over."
    if current_try <= max_tries:
        print("Guess number", current_try)
        guess = int(input("Pick a number between 1 and 10: "))

        # If the guess is equal to the number print out the winning statement.
        if guess == number:
          print("Congratulations, that is correct!")

          # This causes the while loop to stop.
          running = False

        # If the guess is less than the number print out a statement advising them to guess higher 
        # and increase the "current_try" variable by 1.
        elif guess < number:
            print("No, it's a little higher than that.")
            current_try = current_try + 1

        # If neither of the above are true (so they guessed higher than the number) print out a statement advising them to guess lower 
        # and increase the "current_try" variable by 1.
        else:
            print("No, it's a little lower than that.")
            current_try = current_try + 1

    else:
        print("Game Over.")
        running = False

# Once the "while" loop has completed print out the finished message.
else:
    print("Goodbye.")