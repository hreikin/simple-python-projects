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
import pathlib
import os
import pickle

class Person():
    def __init__(self, name = "", email = "", phone = "", address = ""):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class AddressBookApp():
    def __init__(self):
        super().__init__()
        self.save_location = "address-book/address_book.data"
        self.address_book = {}
        if os.path.exists(self.save_location):
            with open(self.save_location, "rb") as savefile:
                self.address_book = pickle.load(savefile)
        else:
            self.address_book = {}

    def save_details(self):
        with open(self.save_location, "wb") as savefile:
            self.address_book = pickle.dump(self.address_book, savefile)
        with open(self.save_location, "rb") as savefile:
            self.address_book = pickle.load(savefile)


    def view_all(self):
        if self.address_book:
            for contact in self.address_book.keys():
                print(contact)
        else:
            print("No contacts found.")

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

myclass = AddressBookApp()

myclass.view_all()
myclass.add_contact()
myclass.view_all()