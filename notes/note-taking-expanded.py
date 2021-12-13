import os
import platform
import logging
import subprocess


DEFAULT_EDITOR = 'notepad'
ANOTHER_NOTE_QUESTION = "Do you want to create another note (yes/no) ? "
############################################## Define Functions ##############################################
# Opens the systems default editor in the directory the notes are saved.

log = logging.info


################################################ Setup Logging ################################################
# Initialize the logger and specify the level of logging. This will log "DEBUG" and higher
# messages to file and log WARNING and higher messages to the console.
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%d-%m-%y %H:%M:%S',
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


############################################## Variable Defaults ##############################################
# Default values for variables.
running = True
editor = os.getenv("EDITOR")

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


def main():
    options = {
        'create': {
            'title':"Create a new note.",
            'func': create_note
        },

        'edit': {
            'title':"Edit an existing note.",
            'func': edit_note
        },

        'delete': {
            'title':"Delete a note.",
            'func': delete_note
        },

        'list': {
            'title':"List all notes.",
            'func': list_notes
        },
    }
    # global options

    r = derek_loop(options)
    print("Goodbye!")
    log("Application closing.")
    return r


def ask_number(q=None):
    default = "Type in a number to make a selection: "
    try:
        val = input(q or default)
        int_val = int(val)
    except ValueError as e:
        print("woops; that's not a number...")
        return ask_number(q)

    return int_val


def as_mode(q=None):

    int_val = ask_number(q)

    funcs = [
        create_note,
        edit_note,
        delete_note,
        list_notes,
    ]

    my_func = funcs[int_val - 1]
    my_func()

    # Takes the users input and runs the appropriate function. If the input is invalid it asks
    # the user to try again.
    if val == "1":
        log("Create mode selected")
        create_note()
    elif val == "2":
        log("Edit mode selected")
        edit_note()
    elif val == "3":
        log("Delete mode selected")
        delete_note()
    elif val == "4":
        log("List mode selected")
        list_notes()
    elif val == "5":
        log("Exit mode selected")
        print("Ok, exiting program now.")
        running = False
    else:
        logging.warning("Not a valid choice, please try again.")



def print_options(options):
    """Prints something like this for a dict of options:

    e.g. from complex options:

        1. Create a note.
        2. Edit a note.
        3. Delete a note.
        4. List all notes.
        5. Exit/Quit

    example:

        >>> print_options({ 'key': {'title': 'apples', 'other': {'title': 'egg'} }})
        1. apples
        2. egg


    """
    for index, (key, sub_dict) in enumerate(options.items()):
        row = f"{index+1}. {sub_dict['title']}"
        print(row)



def close_statement():
    print("Ok, exiting program now.")
    return False


def derek_loop(options):
    ############################################## Application Start ##############################################
    # Runs the program and shows the user a menu to select items from. When an item is selected it
    # runs the corresponding function. If the input is invalid it asks the user to try again.

    running = True

    while running:

        print("\nWelcome to the note taking app.")
        print_options(options)

        q = "Type in a number to make a selection: "
        # current_selection = input(q)
        int_current_selection = ask_number(q)

        choices = tuple(options.values())
        # Takes the users input and runs the appropriate function. If the input is invalid it asks
        # the user to try again.
        try:
            selection = choices[int_current_selection-1]
        except IndexError:
            print('option does not exist...')
            selection = {
                'title': "Exit mode selected",
                'func': close_statement,
            }

        log(selection['title'])
        #run our found function
        func = selection['func']
        running = func()
        if running is None:
            running = True



def create_note():
    try:
        run_main_loop()
    finally:
        print("Returning to main menu.")
        log("Creating finished.")
        log("Returning to main menu.")


def run_main_loop():
    print("\nOk, lets create a note.")
    ask_to_retry = True
    while ask_to_retry:
        ask_to_retry = True
        log("Opening text editor for file creation.")
        # name = str(editor or DEFAULT_EDITOR)
        name = editor

        if name is None:
            print(f'Oops. Please set your editor. Default is: {DEFAULT_EDITOR}')
            name = DEFAULT_EDITOR

        # Opens the systems default editor.
        subprocess.call(name, cwd=save_location, bufsize=1)
        inner_loop()

    print('End of run_main_loop')


def inner_loop():
    # Asks if the user wants to add another note, if they don't it returns them to the
    # main menu.
    ask_to_retry = True
    while ask_to_retry:
        log("Closing text editor.")
        ask_to_retry = input(ANOTHER_NOTE_QUESTION).lower()

        is_yes = True if ask_to_retry in 'yes' else False
        is_no = True if ask_to_retry in 'no' else False

        if (is_yes and is_no) is False:
            # validate the user said something normal.
            print(f'You\'ve said "{ask_to_retry}" - this means nothing')
            ask_to_retry = True
            continue

        # only checked is any one of the switches from above is true.
        creating = is_yes
        ask_to_retry = False

        print_val = "\nOk, thank you."
        if is_yes:
            print_val = "\nOk, let's carry on then."
        # if is_no:

        print(print_val)


# Asks the user for a file name and then opens it. If it doesn't exist it shows an error and
# returns to the main menu.
def edit_note():
    try:
        print("\nOk, lets edit a note.")
        editing = True

        # Asks the user for a filename and creates the full path for it.
        while editing:
            ask_to_retry = True

            # Show the user a list of their notes so they can see the filenames.
            print("\nHere is a list of your notes:\n")
            log(f"Listing notes in \"{save_location}\".")
            list_of_notes = os.listdir(save_location)
            for note in list_of_notes:
                print(note)

            file_name = input("\nWhat is the files name ? ")
            full_filepath = os.path.join(save_location, file_name)

            # Checks if the file exists before opening the editor, if it doesn't it prints an
            # error to the console and logs it the log file.
            if os.path.exists(full_filepath):
                log(f"Opening \"{full_filepath}\".")
                subprocess.call(f"{editor} {full_filepath}", bufsize=1, shell=True)
            else:
                logging.error(f"The file \"{full_filepath}\" does not exist.")
                log("Returning to the menu.")

            # Asks the user if they want to edit another note, if they don't it returns them
            # to the main menu.
            while ask_to_retry:
                ask_to_retry = input("Do you want to edit another note (yes/no) ? ")
                if ask_to_retry.lower() in "yes":
                    print("\nOk, let's carry on then.")
                    ask_to_retry = False
                elif ask_to_retry.lower() in "no":
                    print("\nOk, thank you.")
                    ask_to_retry = False
                    editing = False
                else:
                    logging.warning("Invalid input, please try again.")
                    ask_to_retry = True
            else:
                ask_to_retry = False
        else:
            editing = True
    finally:
        print("Editing Finished, returning to main menu.")
        log("Editing finished.")
        log("Returning to main menu.")


def ask_question(q=None):
    DEF = f"Are you sure you do this action (yes/no) ? "
    q = q or DEF
    val = input(q).lower()

    if val.lower() in "yes":
        return True


    if val.lower() in "no":
        return False

    # is deffo not 'yes' or 'no'
    print('Woops...')
    return ask_question(q)

# Asks for the file name and extension of the note to be deleted and deletes it after a confirmation.
# If the file doesn't exist it reports an error and returns to the main menu.
def delete_note():
    try:
        deleting = True
        while deleting:
            ask_to_retry = True
            confirm_delete = True

            # Show the user a list of their notes so they can see the filenames.
            print("\nHere is a list of your notes:\n")
            log(f"Listing notes in \"{save_location}\".")
            list_of_notes = os.listdir(save_location)
            for note in list_of_notes:
                print(note)

            # Ask for the name and extension of the note they would like to delete.
            deleted_note = input("\nGive the file name and its extension of the note you want to delete: ")
            full_filepath = os.path.join(save_location, deleted_note)

            # Confirms the user wants to delete the file, if they don't it cancels and asks if they would like
            # to delete another note.

            def_q = f"Are you sure you want to delete {deleted_note} (yes/no) ? "
            confirm_delete = ask_question(def_q)

            if confirm_delete:
                logging.warning(f"Deleting \"{deleted_note}\".")

                # Checks if the file exists before deleting it, if it doesn't exist it prints an error
                # to the console and logs it to the log file.
                if os.path.exists(full_filepath):
                    os.remove(full_filepath)
                    logging.warning(f"\"{deleted_note}\" has been deleted.")
                    confirm_delete = False
                else:
                    logging.error(f"The file \"{full_filepath}\" does not exist.")
                    confirm_delete = False
            else:
                print("Ok, cancelling.")
                log(f"Deleting \"{full_filepath}\" cancelled.")

                log("Deleting '{}' cancelled.", full_filepath)

                log(f"""Deleting "{full_filepath}" cancelled.""")

                confirm_delete = False


            # Asks the user if they want to delete another note, if they don't it returns them to the main menu.
            while ask_to_retry:
                ask_to_retry = input("Do you want to delete another note (yes/no) ? ")
                if ask_to_retry.lower() in "yes":
                    print("\nOk, let's carry on then.")
                    ask_to_retry = False
                elif ask_to_retry.lower() in "no":
                    print("\nOk, thank you.")
                    ask_to_retry = False
                    deleting = False
                else:
                    logging.warning("Invalid input, please try again.")
                    ask_to_retry = True
            else:
                ask_to_retry = False
        else:
            deleting = True
    finally:
        print("Returning to main menu.")
        log("Deleting finished.")
        log("Returning to main menu.")


# Lists all the notes in the default directory and waits for user input before returning to the main menu.
def list_notes():
    try:
        print("\nHere is a list of your notes:\n")
        log(f"Listing notes in \"{save_location}\".")
        list_of_notes = os.listdir(save_location)
        for note in list_of_notes:
            print(note)
        input("\nPress any key to return to the menu.")
    finally:
        print("Returning to main menu.")
        log("Listing finished.")
        log("Returning to main menu.")



if __name__ == '__main__':
    main()
