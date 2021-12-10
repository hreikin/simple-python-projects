# Import "seed" and "randint" modules for random number generation and the "sleep" module for the sleep function.
from random import seed
from random import randint
from time import sleep

# Seed the random number generation. This method uses the users system time.
seed()

# Set variable default values.
roll_again = True
number_of_dice = 0
current_dice_roll = 1

# Rolls the dice and prints out the values.
while roll_again:
    number_of_dice = int(input("How many dice do you want to roll ? "))
    print("Ok, let's roll the dice.")
    print("Rolling...")
    sleep(0.5)

    # Prints out the dice roll result(s) until the amount (number_of_dice) selected by the user is reached. 
    # When finished it resets the "current_dice_roll" back to its default value.
    while current_dice_roll <= number_of_dice:
        print("Dice number", current_dice_roll, "is a value of:", randint(1, 6))
        current_dice_roll += 1
    else:
        current_dice_roll = 1

    # Ask if the user wants to roll again.
    roll_again = input("Do you want to roll again (yes/no) ? ")
    
    # Check the users answer and either restart the loop or end it.
    if roll_again.lower().startswith("y") or roll_again.upper().startswith("Y"):
            print("Ok, let's carry on then.")
    elif roll_again.lower().startswith("n") or roll_again.upper().startswith("N"):
            print("Ok, thank you.")
            roll_again = False
else:
    print("Goodbye!")