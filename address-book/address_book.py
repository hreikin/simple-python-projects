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

    def add_contact(self):
        while True:
            print("Ok, let's add a new contact. Please provide the following info.")
            name = input("Name: ").title()
            if name in self.address_book:
                print("A contact is already present with that name.")
                pass
            else:
                email = input("Email: ")
                phone = input("Phone Number: ")
                address = input("Address: ").title()
                self.address_book[name] = Person(name, email, phone, address)
                self.save_details()
                print("Contact successfully added.")
            if self.ask_question() == False:
                return

    def edit_contact(self):
        while True:
            print("Ok, let's edit a contact. Please provide the contacts name.")
            old_name = input("Name: ").title()
            if old_name not in self.address_book:
                    print("There is no contact by that name.")
                    pass
            print("Input the new information below.")
            new_name = input("Name: ").title()
            new_email = input("Email: ")
            new_phone = input("Phone Number: ")
            new_address = input("Address: ").title()
            if self.ask_question(None) == True:
                self.address_book.pop(old_name)
                self.address_book[new_name] = Person(new_name, new_email, new_phone, new_address)
                self.save_details()
                print("Contact successfully updated.")
            if self.ask_question() == False:
                return

    def delete_contact(self):
        while True:
            name = input("What is the name of the contact you wish to delete: ").title()
            if name not in self.address_book:
                print("There is no contact by that name.")
                pass
            # confirm_delete = f"Are you sure you want to delete the info for {name.title()} (yes/no) ? "
            elif self.ask_question(None) == True:
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


myperson = Person()
myclass = AddressBookApp()

# Testing things work.
myclass.view_all()
myclass.add_contact()
myclass.view_all()
myclass.delete_contact()
myclass.view_all()
myclass.edit_contact()
myclass.view_all()