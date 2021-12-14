import os
import platform
import logging
import subprocess


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


