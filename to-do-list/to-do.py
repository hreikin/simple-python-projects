import sys
import logging
import pickle
import os

running = True

to_do_file = "to-do-list/to-do.data"

if os.path.exists(to_do_file):
    with open(to_do_file, "rb") as readfile:
        to_do_list = pickle.load(readfile)
else:
    to_do_list = []

def add_item():
    with open(to_do_file, "wb") as writefile:
        new_item = input("What do you want to add ? ")
        to_do_list.append(new_item)
        pickle.dump(to_do_list, writefile)
        logging.info(f"\"{new_item}\" has been added to the list.")

def show_list():
    if os.path.exists(to_do_file):
        with open(to_do_file, "rb") as readfile:
            to_do_list = pickle.load(readfile)
            for index, item in enumerate(to_do_list, start = 1):
                print(f"{index}. {item}")
    else:
        logging.info("No items in the list.")

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
    4. Sort items.
    5. Mark an item complete.
    6. Show \"To Do\" list.
    7. Show \"Completed\" items.
    8. Exit/Quit.
    """)

    current_selection = input("Type in a number to make a selection: ")

    # Takes the users input and runs the appropriate function. If the input is invalid it asks 
    # the user to try again.
    if current_selection == "1":
        logging.info("Ok, lets create an item.")
        add_item()
    elif current_selection == "2":
        logging.info("Ok, lets edit an item.")
    elif current_selection == "3":
        logging.info("Ok, lets delete an item.")
    elif current_selection == "4":
        logging.info("Ok, lets sort the items.")
    elif current_selection == "5":
        logging.info("Ok, lets mark an item complete.")
    elif current_selection == "6":
        logging.info("Ok, lets show the \"To Do\" list.")
        show_list()
    elif current_selection == "7":
        logging.info("Ok, lets show the \"Completed\" list.")
    elif current_selection == "8":
        logging.info("Ok, exiting program now.")
        running = False
    else:
        logging.info("Not a valid choice, please try again.")
else:
    logging.info("Goodbye!")
    sys.exit(0)