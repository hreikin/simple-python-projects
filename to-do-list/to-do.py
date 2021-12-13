import sys
import logging
import pickle
import os

# Set default values for variables.
running = True
to_do_file = "to-do-list/to-do.data"

# import json
# from pathlib import Path
# shelve, yaml, json
# collections.defaultdict
#

# Checks if file exists and loads it, if it doesn't sets the list to empty.
if os.path.exists(to_do_file):
    with open(to_do_file, "rb") as readfile:
        to_do_list = pickle.load(readfile)
else:
    to_do_list = []


def main():

    ################################################ Setup Logging ################################################
    # Initialize the logger and specify the level of logging. This will log "DEBUG" and higher
    # messages to file and log WARNING and higher messages to the console.
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-8s %(levelname)-8s %(message)s',
                        datefmt='%d-%m-%y %H:%M:%S',
                        filename='to-do-list/app.log',
                        filemode='w')

    # Define a "handler" which writes "INFO" messages or higher to the "sys.stderr".
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    # Set a format which is simpler for console messages. This just prints the message with no other details.
    formatter = logging.Formatter('%(message)s')

    # Tell the console "handler" to use this format.
    console.setFormatter(formatter)

    # Add the "handler" to the "root logger".
    logging.getLogger('').addHandler(console)

    while running:

        print("\n Welcome to the \"To Do\" app.")
        print("""
        1. Create an item.
        2. Edit an item.
        3. Delete an item.
        4. Show \"To Do\" list.
        5. Exit/Quit.
        """)

        current_selection = input("Type in a number to make a selection: ")

        # Takes the users input and runs the appropriate function. If the input is invalid it asks
        # the user to try again.
        if current_selection == "1":
            logging.info("Ok, lets create an item.")
            add_item()
        elif current_selection == "2":
            logging.info("Ok, lets edit an item.")
            edit_item()
        elif current_selection == "3":
            logging.info("Ok, lets delete an item.")
            delete_item()
        elif current_selection == "4":
            logging.info("Ok, lets show the \"To Do\" list.")
            show_list()
        elif current_selection == "5":
            logging.info("Ok, exiting program now.")
            running = False
        else:
            logging.info("Not a valid choice, please try again.")
    else:
        logging.info("Goodbye!")
        sys.exit(0)


# tdp = Path(to_do_file)
# to_do_list = pickle.loads(tdp.read_text() if tdp.exists() else '[]')

# Asks the user what they want to add to the list and appends it to the bottom and saves the file.
def add_item():
    with open(to_do_file, "wb") as writefile:
        new_item = input("What do you want to add ? ")
        to_do_list.append(new_item)
        pickle.dump(to_do_list, writefile)
        logging.info(f"\"{new_item}\" has been added to the list.")


# Asks the user which item they would like to edit and what the new content is before saving.
def edit_item():
    for index, item in enumerate(to_do_list, start = 1):
        print(f"{index}. {item}")

    with open(to_do_file, "wb") as editfile:
        edited_item = int(input("Enter the number of the item you want to edit: "))
        edited_item -= 1
        edited_item_input = input("What would you like to change it to ? ")
        to_do_list[edited_item] = edited_item_input
        pickle.dump(to_do_list, editfile)
        logging.info(f"Item number {edited_item + 1} has been edited.")


# Asks the user which item they would like to delete and then removes it and saves the list file.
def delete_item():
    for index, item in enumerate(to_do_list, start = 1):
        print(f"{index}. {item}")

    with open(to_do_file, "wb") as deletefile:
        delete_item = int(input("Enter the number of the item you want to delete: "))
        delete_item -= 1
        to_do_list.pop(delete_item)
        pickle.dump(to_do_list, deletefile)
        logging.info(f"Item number {delete_item + 1} has been removed.")


# Shows the user the current list and waits for input before returning to the menu. If no file exists
# it prints a message explaining so and waits for input.
def show_list():
    if os.path.exists(to_do_file):
        with open(to_do_file, "rb") as readfile:
            to_do_list = pickle.load(readfile)
            for index, item in enumerate(to_do_list, start = 1):
                print(f"{index}. {item}")
            input("Press ENTER to return to the menu. ")
    else:
        logging.info("No items in the list.")
        input("Press ENTER to return to the menu. ")

if __name__ == '__main__':
    main()
