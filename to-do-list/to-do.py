running = True
to_do_list = []
completed = []

while running:

    print("\n Welcome to the To Do app.")
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
        print("Ok, lets create an item.")
    elif current_selection == "2":
        print("Ok, lets edit an item.")
    elif current_selection == "3":
        print("Ok, lets delete an item.")
    elif current_selection == "4":
        print("Ok, lets sort the items.")
    elif current_selection == "5":
        print("Ok, lets mark an item complete.")
    elif current_selection == "6":
        print("Ok, lets show the \"To Do\" list.")
    elif current_selection == "7":
        print("Ok, lets show the \"Completed\" list.")
    elif current_selection == "8":
        print("Ok, exiting program now.")
        running = False
    else:
        print("Not a valid choice, please try again.")
else:
    print("Goodbye!")