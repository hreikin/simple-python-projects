import os
import platform
import logging
import subprocess

# Default values for variables.
running = True
editor = os.getenv("EDITOR")

# Initialize the logger and specify the level of logging. This will create/rewrite a log file.
logging.basicConfig(
    level = logging.DEBUG,
    filename = "notes/app.log",
    filemode = "w",
    format = "%(asctime)s - %(levelname)s - %(message)s"
    )

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

# Opens up the systems default editor in the directory the notes are saved.
def create_note():
    try:
        print("\nOk, lets create a note.")
        logging.info("Opening text editor for file creation.")
        subprocess.call(f"{editor}", cwd=save_location, bufsize=1)
    finally:
        print("Text editor closed, returning to main menu.")
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
        if os.path.exists(full_filepath):
            subprocess.call(f"{editor} {full_filepath}", bufsize=1, shell=True)
        else:
            print(f"ERROR: The file {full_filepath} does not exist.")
            logging.error(f"ERROR: The file {full_filepath} does not exist.")
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
        confirm_delete = input(f"Are you sure you want to delete {deleted_note} (yes/no) ? ")
        if confirm_delete.lower() in "yes":
                print(f"Ok, deleting \"{deleted_note}\".")
                logging.warning(f"Deleting \"{deleted_note}\".")
                if os.path.exists(full_filepath):
                    os.remove(full_filepath)
                    print(f"{deleted_note} has been deleted.")
                    logging.warning(f"{deleted_note} has been deleted.")
                else:
                    print(f"ERROR: The file {full_filepath} does not exist.")
                    logging.error(f"ERROR: The file {full_filepath} does not exist.")
        elif confirm_delete.lower() in "no":
                print("Ok, cancelling.")
                logging.info(f"Deleting cancelled.")
    finally:
        print("Returning to main menu.")
        logging.info("Returning to menu.")

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
    print("\nWelcome to the note taking app.")
    print("""
    1. Create a note.
    2. Edit a note.
    3. Delete a note.
    4. List all notes.
    5. Exit/Quit
    """)

    current_selection = input("Type in a number to make a selection: ")

    if current_selection == "1":
        create_note()
    elif current_selection == "2":
        edit_note()
    elif current_selection == "3":
        delete_note()
    elif current_selection == "4":
        list_notes()
    elif current_selection == "5":
        print("Ok, exiting program now.")
        running = False
    else:
        print("Not a valid choice, please try again.")
else:
    print("Goodbye!")