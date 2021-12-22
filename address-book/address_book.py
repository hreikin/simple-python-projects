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
            # return self.retry_question()
            # if self.ask_question() == False:
            #     return
                
    def add_contact(self):
        while True:
            print("Ok, let's add a new contact. Please provide the following info.")
            name, email, phone, address = self.get_details()
            if self.ask_question(None) == True:
                self.address_book[name] = Person(name, email, phone, address)
                self.save_details()
                print("Contact added successfully.")
            # return self.retry_question()
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
            if self.ask_question() == False:
                return

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

    def __str__(self):
        return MENU

MENU = """
Welcome to the address book app

1. View contacts
2. Add new contact
3. Update contact
4. Delete contact
5. Exit
""".title()

def main():
    app = AddressBookApp()
    choice = ""
    while choice != "5":
        print(app)
        choice = input("Make a selection: ")
        if choice == "1":
            app.view_all()
        elif choice == "2":
            app.add_contact()
        elif choice == "3":
            app.edit_contact()
        elif choice == "4":
            app.delete_contact()
        elif choice == "5":
            print("\nExiting now. Goodbye!")            
        else:
            print("\nInvalid input, please try again.")

if __name__ == '__main__':
    main()