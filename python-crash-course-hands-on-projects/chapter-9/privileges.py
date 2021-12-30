# Write a separate Privileges class. The class should have one attribute, 
# privileges, that stores a list of strings as described in "admin.py". Move the 
# show_privileges() method to this class. Make a Privileges instance as an 
# attribute in the Admin class. Create a new instance of Admin and use your 
# method to show its privileges.

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

admin = Admin("Super", "User", 33, "Everywhere")
admin.describe_user()
admin.privileges.show_privileges()

print("Adding privileges.")
new_privileges = ["can add post", "can delete post" , "can ban user"]
admin.privileges.privileges = new_privileges
admin.privileges.show_privileges()