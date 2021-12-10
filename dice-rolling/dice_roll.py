# Import "seed" and "randint" modules for random number generation and the "sleep" module for the sleep function.
from random import seed
from random import randint
from time import sleep

# Seed the random number generation. This method uses the users system time.
seed()

roll_again = True

while roll_again:
    print("Let's roll two dice.")
    print("Rolling...")
    sleep(1)
    print("The values are: ")
    print("Value 1 is: ", randint(1, 6))
    print("Value 2 is: ", randint(1, 6))

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