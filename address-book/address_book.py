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
        super().__init__()
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
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone Number: ")
        address = input("Address: ")
        if name not in self.address_book:
            self.address_book[name] = Person(name, email, phone, address)
            self.save_details()
        else:
            print("Contact is already present.")


myperson = Person()
myclass = AddressBookApp()

myclass.view_all()
# myclass.add_contact()
# myclass.view_all()