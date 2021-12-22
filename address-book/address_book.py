##################################### TASK ######################################
# Create your own command-line address-book program which you can browse, add, 
# modify, delete or search through for your contacts such as friends, family and 
# colleagues and their information such as email address and/or phone number. 
# Details must be stored for later retrieval.

##################################### HINT ######################################
# Create a class to represent the person's information. Use a dictionary to store 
# person objects with their name as the key. Use the pickle module to store the 
# objects persistently on your hard disk. Use the dictionary built-in methods to 
# add, delete and modify the persons.
from pathlib import Path
import pickle
import sys

class Person(object):
    def __init__(self, name = "", email = "", phone = "", address = ""):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class AddressBookApp(object):
    def __init__(self):
        self.save_location = Path("address-book/address_book.data")
        self.address_book = {}
        if self.save_location.exists():
            with open(self.save_location, "rb") as savefile:
                self.address_book = pickle.load(savefile)
        else:
            self.address_book = {}

    def save_details(self):
        with open(self.save_location, "wb") as savefile:
            pickle.dump(self.address_book, savefile)

    def print_line(self, **info):
        print(f"{info['name']:<25} {info['email']:<25} {info['phone']:<25} {info['address']:<25}")

    def view_all(self):
        if not self.address_book:
            print("No contacts found.")
            return
        self.print_line(name="Name", email="Email", phone="Phone", address="Address")
        for info in self.address_book.values():
            self.print_line(**vars(info))
        input("\nPress ENTER to return to the menu.")

    def get_details(self):
        while True:
            name = input("Name: ").title()
            if name in self.address_book:
                print("A contact is already present with that name.")
                pass
            else:
                email = input("Email: ")
                phone = input("Phone Number: ")
                address = input("Address: ").title()
                return name, email, phone, address
                
    def add_contact(self):
        while True:
            print("Ok, let's add a new contact. Please provide the following info.")
            name, email, phone, address = self.get_details()
            if self.ask_question(None) == True:
                self.address_book[name] = Person(name, email, phone, address)
                self.save_details()
                print("Contact added successfully.")
            # self.retry_question()
            if self.ask_question() == False:
                return

    def edit_contact(self):
        while True:
            print("Ok, let's edit a contact. Please provide the contacts name.")
            old_name = input("Name: ").title()
            if old_name not in self.address_book:
                    print("There is no contact by that name.")
                    pass
            else:
                print("Input the new information below.")
                name, email, phone, address = self.get_details()
                if self.ask_question(None) == True:
                    self.address_book.pop(old_name)
                    self.address_book[name] = Person(name, email, phone, address)
                    self.save_details()
                    print("Contact successfully updated.")
            # self.retry_question()
            if self.ask_question() == False:
                return

    def delete_contact(self):
        while True:
            name = input("What is the name of the contact you wish to delete: ").title()
            confirm_delete = f"Are you sure you want to delete the info for {name.title()} (yes/no) ? "
            if name not in self.address_book:
                print("There is no contact by that name.")
                pass
            elif self.ask_question(confirm_delete) == True:
                self.address_book.pop(name)
                print(f"Ok, {name} is deleted.")
                self.save_details()
            # self.retry_question()
            if self.ask_question() == False:
                return
    
    def search_contact(self):
        search_name = input("What is the name of the contact you wish to search for: ").title()
        if search_name not in self.address_book:
            print("There is no contact by that name.")
        else:
            search_item = self.address_book[search_name]
            for key, value in vars(search_item).items():
                print(key + ":", value)
        input("\nPress ENTER to return to the menu.")


    def ask_question(self, question="Do you want to do this action again (yes/no) ? "):
        CONFIRM = "Are you sure you want to do this (yes/no) ? "
        ask = question or CONFIRM
        val = input(ask).lower()
        if val.lower() in "yes":
            return True
        if val.lower() in "no":
            print("OK, cancelling.")
            return False
        # Invalid input response.
        print('Invalid input, please try again.')
        return self.ask_question(question)

    def retry_question(self):
        ask_to_retry = self.ask_question()
        return ask_to_retry

    def print_options(self, options):
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

    def main_loop(self, options):
        ############################################## Application Start ##############################################
        # Runs the program and shows the user a menu to select items from. When an item is selected it
        # runs the corresponding function. If the input is invalid it asks the user to try again.

        running = True

        while running:

            print("\nWelcome to the address book app.")
            self.print_options(options)

            q = "Type in a number to make a selection: "
            # current_selection = input(q)
            int_current_selection = self.ask_number(q)

            choices = tuple(options.values())
            # Takes the users input and runs the appropriate function. If the input is invalid it asks
            # the user to try again.
            try:
                selection = choices[int_current_selection-1]
            except IndexError:
                print('option does not exist...')
                selection = {
                    'title': "Exit mode selected",
                    'func': self.close_statement,
                }

            print(selection['title'])
            #run our found function
            func = selection['func']
            running = func()
            if running is None:
                running = True

    def ask_number(self, q=None):
        default = "Type in a number to make a selection: "
        try:
            val = input(q or default)
            int_val = int(val)
        except ValueError as e:
            print("woops; that's not a number...")
            return self.ask_number(q)

        return int_val


    # def as_mode(self, q=None):

    #     int_val = self.ask_number(q)

    #     funcs = [
    #         self.view_all,
    #         self.search_contact,
    #         self.add_contact,
    #         self.edit_contact,
    #         self.delete_contact,
    #         self.close_statement,
    #     ]

    #     my_func = funcs[int_val - 1]
    #     my_func()

        # Takes the users input and runs the appropriate function. If the input is invalid it asks
        # the user to try again.
        # if int_val == "1":
        #     self.view_all()
        # elif int_val == "2":
        #     self.search_contact()
        # elif int_val == "3":
        #     self.add_contact()
        # elif int_val == "4":
        #     self.edit_contact()
        # elif int_val == "5":
        #     self.delete_contact()
        # elif int_val == "6":
        #     sys.exit()
        # else:
        #     print("Not a valid choice, please try again.")

    def close_statement(self):
        print("Ok, exiting program now.")
        return False

#     def __str__(self):
#         return MENU

# MENU = """
# Welcome to the address book app

# 1. View contacts
# 2. Search for a contact
# 3. Add new contact
# 4. Update contact
# 5. Delete contact
# 6. Exit
# """.title()

# def main():
#     app = AddressBookApp()
#     choice = ""
#     while choice != "6":
#         print(app)
#         choice = input("Make a selection: ")
#         if choice == "1":
#             app.view_all()
#         elif choice == "2":
#             app.search_contact()
#         elif choice == "3":
#             app.add_contact()
#         elif choice == "4":
#             app.edit_contact()
#         elif choice == "5":
#             app.delete_contact()
#         elif choice == "6":
#             print("\nExiting now. Goodbye!")            
#         else:
#             print("\nInvalid input, please try again.")

def main():
    app = AddressBookApp()
    options = {
        'view': {
            'title':"View all contacts.",
            'func': app.view_all
        },
        'search': {
            'title':"Search all contacts.",
            'func': app.search_contact
        },
        'add': {
            'title':"Add a new contact.",
            'func': app.add_contact
        },

        'edit': {
            'title':"Edit an existing contact.",
            'func': app.edit_contact
        },

        'delete': {
            'title':"Delete a contact.",
            'func': app.delete_contact
        },

        'exit': {
            'title':"Exit the program.",
            'func': app.close_statement
        },

    }
    # global options

    run = app.main_loop(options)
    print("Goodbye!")
    return run

if __name__ == '__main__':
    main()