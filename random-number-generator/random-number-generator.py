# Import "seed" and "randint" modules for random number generation.
from random import seed
from random import randint
from time import sleep
import logging

# Seed the random number generation. This method uses the users system time.
seed()

# Set variable default value.
amount_of_numbers = range(0, 1)
min_number = 1
max_number = 1
continue_generating = True
ask_to_retry = True

# Initialize the logger and specify the level of logging.
logging.basicConfig(
    level = logging.DEBUG,
    format = "%(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("random-number-generator/debug.log", mode = "w"),
        logging.StreamHandler()
    ]
)

print("Welcome to the random number generator, lets generate some random numbers.")

# Generates random number(s) based on user input.
while continue_generating:
    try:
        print("How many numbers do you want to generate ? ", end="")
        amount_of_numbers = range(0, int(input()))

        # If the length of the range "amount_of_numbers" is greater than zero carry on, if not print out a message 
        # about invalid input and restart.
        if len(amount_of_numbers) > 0:
            min_number = int(input("What is the lowest number you want to generate from ? "))

            # If the "min_number" is greater than zero carry on, if not print out a message about invalid input and 
            # restart from the beginning.
            if min_number > 0:
                max_number = int(input("What is the highest number you want to generate to ? "))

                # Check the "max_number" is higher than the "min_number", if not print out a message about invalid 
                # input and restart from the beginning.
                if max_number > min_number:
                    print(f"Ok, lets generate {len(amount_of_numbers)} number(s) between {min_number} and {max_number}")
                    print("Generating number(s) now...")
                    sleep(0.5)

                    # Iterate through the "amount_of_numbers" generating a random number for each one.
                    for amount in amount_of_numbers:
                        print(f"Generated number {amount + 1} is: {randint(1, max_number)}")

                    while ask_to_retry:
                        # Ask if the user wants to roll again. If the input is invalid then ask again.
                        continue_generating = input("Do you want to generate another random number (yes/no) ? ")
                        
                        # Check the users answer and either restarts the program or exits it.
                        if continue_generating.lower() in "yes":
                                print("Ok, let's carry on then.")
                                ask_to_retry = False
                        elif continue_generating.lower() in "no":
                                print("Ok, thank you.")
                                continue_generating = False
                                ask_to_retry = False
                        else:
                            logging.info("Invalid input, please try again.")
                    else:
                        ask_to_retry = True
                else:
                    logging.info("Invalid input, please start again.")
            else:
                logging.info("Invalid input, please start again.")
        else:
            logging.info("Invalid input, please start again.")
    except:
        logging.info("Invalid input, please start again.")
else:
    print("Goodbye!")