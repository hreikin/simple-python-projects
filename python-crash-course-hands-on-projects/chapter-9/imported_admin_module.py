# Start with your work from "admin.py". Store the classes User, Privileges and 
# Admin in one module. Create a separate file, make an Admin instance, and call 
# show_privileges() to show that everything is working correctly.

class User():
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"""
        Here are the users details:
        Name: {self.first_name} {self.last_name}
        Age: {self.age}
        Location: {self.location}
        """)

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


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