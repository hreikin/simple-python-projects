# Import "seed" and "randint" modules for random number generation and the "sleep" module for the sleep function.
from random import seed
from random import randint
from time import sleep

# Seed the random number generation. This method uses the users system time.
seed()

# Set variable default values.
roll_again = True
number_of_dice = range(0, 1)
ask_to_retry = True
number_of_sides = 6

print("\nWelcome to the dice rolling app, lets start rolling some dice.\n")

# Rolls the dice and prints out the values.
while roll_again:
    try:
        number_of_sides = int(input("How many sides does the dice have ? "))
        if number_of_sides > 0:
            print("How many dice do you want to roll ? ", end="")
            number_of_dice = range(0, int(input()))
            if len(number_of_dice) > 0:
                print("Ok, let's roll the dice.")
                print("Rolling...")
                sleep(0.5)

                # Prints out the dice roll result(s) until the amount (number_of_dice) selected by the user is reached. 
                # When finished it resets the "current_dice_roll" back to its default value.
                for amount in number_of_dice:
                    print(f"Dice number {amount + 1} is a value of: {randint(1, number_of_sides)}")

                while ask_to_retry:
                    # Ask if the user wants to roll again. If the input is invalid then ask again.
                    roll_again = input("Do you want to roll again (yes/no) ? ")
                    
                    # Check the users answer and either restarts the program or exits it.
                    if roll_again.lower().startswith("y") or roll_again.upper().startswith("Y"):
                            print("Ok, let's carry on then.")
                            ask_to_retry = False
                    elif roll_again.lower().startswith("n") or roll_again.upper().startswith("N"):
                            print("Ok, thank you.")
                            roll_again = False
                            ask_to_retry = False
                    else:
                        print("***Invalid input, please try again.***")
                else:
                    ask_to_retry = True
            else:
                print("***Invalid input, please start again.***")
        else:
            print("***Invalid input, please start again.***")
    except:
        print("***Invalid input, please start again.***")
else:
    print("Goodbye!")