import os
import platform
import logging
import subprocess

# Default values for variables.
running = True
editor = os.getenv("EDITOR")

# Initialize the logger and specify the level of logging. This will log "DEBUG" and higher 
# messages to file and log WARNING and higher messages to the console.
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%d-%m %H:%M:%S',
                    filename='notes/app.log',
                    filemode='w')

# Define a "handler" which writes "WARNING" messages or higher to the "sys.stderr".
console = logging.StreamHandler()
console.setLevel(logging.WARNING)

# Set a format which is simpler for console messages.
formatter = logging.Formatter('%(levelname)s: %(message)s')

# Tell the console "handler" to use this format.
console.setFormatter(formatter)

# Add the "handler" to the "root logger".
logging.getLogger('').addHandler(console)

# Check which OS the user has and figure out and join the home drive, path and "save_location" 
# for windows, or just home directory and "save_location" for linux/mac. We use "os.path.join" 
# instead of joining strings to ensure the path has the correct format expected by the users 
# operating system.
if platform.platform().startswith("Windows"):
    save_location = os.path.join(os.getenv("HOMEDRIVE"),
                                os.getenv("HOMEPATH"),
                                "python-notes/")
else:
    save_location = os.path.join(os.getenv("HOME"),
    "python-notes/")

# Opens the systems default editor in the directory the notes are saved.
def create_note():
    try:
        print("\nOk, lets create a note.")
        creating = True
        while creating:
            ask_to_retry = True
            logging.info("Opening text editor for file creation.")
            subprocess.call(f"{editor}", cwd=save_location, bufsize=1)
            while ask_to_retry:
                ask_to_retry = input("Do you want to create another note (yes/no) ? ")
                if ask_to_retry.lower() in "yes":
                    print("\nOk, let's carry on then.")
                    ask_to_retry = False
                elif ask_to_retry.lower() in "no":
                    print("\nOk, thank you.")
                    ask_to_retry = False
                    creating = False
                else:
                    logging.warning("Invalid input, please try again.")
                    ask_to_retry = True
            else:
                ask_to_retry = False
        else:
            creating = True
    finally:
        print("Returning to main menu.")
        logging.info("Closing text editor.")
        logging.info("Returning to main menu.")

# Asks the user for a file name and then opens it. If it doesn't exist it shows an error and 
# returns to the main menu.
def edit_note():
    try:
        print("\nOk, lets edit a note.")
        file_name = input("What is the files name ? ")
        full_filepath = os.path.join(save_location, file_name)
        logging.info(f"Opening {full_filepath}")

        # Checks if the file exists before opening the editor, if it doesn't it prints an 
        # error to the console and logs it the log file.
        if os.path.exists(full_filepath):
            subprocess.call(f"{editor} {full_filepath}", bufsize=1, shell=True)
        else:
            logging.error(f"The file {full_filepath} does not exist.")
            logging.info("Returning to the main menu.")
    finally:
        print("Text editor closed, returning to main menu.")
        logging.info("Closing text editor.")
        logging.info("Returning to main menu.")

# Asks for the file name and extension of the note to be deleted and deletes it after a confirmation. 
# If the file doesn't exist it reports an error and returns to the main menu.
def delete_note():
    try:
        deleted_note = input("\nGive the file name and its extension of the note you want to delete: ")
        full_filepath = os.path.join(save_location, deleted_note)

        # Confirms the user wants to delete the file, if they don't it cancels and returns to the 
        # main menu.
        confirm_delete = input(f"Are you sure you want to delete {deleted_note} (yes/no) ? ")
        if confirm_delete.lower() in "yes":
                logging.warning(f"Deleting \"{deleted_note}\".")

                # Checks if the file exists before deleting it, if it doesn't exist it prints an error 
                # to the console and logs it to the log file.
                if os.path.exists(full_filepath):
                    os.remove(full_filepath)
                    logging.warning(f"{deleted_note} has been deleted.")
                else:
                    logging.error(f"The file {full_filepath} does not exist.")
                    
        elif confirm_delete.lower() in "no":
                print("Ok, cancelling.")
                logging.info(f"Deleting cancelled.")
    finally:
        print("Returning to main menu.")
        logging.info("Returning to main menu.")

# Lists all the notes in the default directory and waits for user input before returning to the main menu.
def list_notes():
    try:
        print("\nHere is a list of your notes:\n")
        logging.info(f"Listing notes in \"{save_location}\".")
        list_of_notes = os.listdir(save_location)
        for note in list_of_notes:
            print(note)
        input("\nPress any key to return to the menu.")
    finally:
        print("Returning to main menu.")
        logging.info("Returning to menu.")

# Runs the program and shows the user a menu to select items from. When an item is selected it 
# runs the corresponding function. If the input is invalid it asks the user to try again.
while running:

    logging.info("Application started.")
    print("\nWelcome to the note taking app.")
    print("""
    1. Create a note.
    2. Edit a note.
    3. Delete a note.
    4. List all notes.
    5. Exit/Quit
    """)

    current_selection = input("Type in a number to make a selection: ")

    # Takes the users input and runs the appropriate function. If the input is invalid it asks 
    # the user to try again.
    if current_selection == "1":
        logging.info("Create mode selected")
        create_note()
    elif current_selection == "2":
        logging.info("Edit mode selected")
        edit_note()
    elif current_selection == "3":
        logging.info("Delete mode selected")
        delete_note()
    elif current_selection == "4":
        logging.info("List mode selected")
        list_notes()
    elif current_selection == "5":
        logging.info("Exit mode selected")
        print("Ok, exiting program now.")
        running = False
    else:
        logging.warning("Not a valid choice, please try again.")
else:
    print("Goodbye!")
    logging.info("Application closing.")