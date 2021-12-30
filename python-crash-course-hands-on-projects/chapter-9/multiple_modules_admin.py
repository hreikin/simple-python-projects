# Store the User class in one module, and store the Privileges and Admin classes 
# in a separate module. In a separate file, create an Admin instance and call 
# show_privileges() to show that everything is still working correctly.

from multiple_modules_user import User

class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        if self.privileges:
            for i in self.privileges:
                print(f"- {i}")
        else:
            print("- This user has no privileges.")