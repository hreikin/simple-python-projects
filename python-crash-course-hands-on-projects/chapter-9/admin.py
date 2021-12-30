# An administrator is a special kind of user. Write a class called Admin that 
# inherits from the User class you wrote in "users.py" or "login_attempts.py". 
# Add an attribute, privileges , that stores a list of strings like 
# "can add post", "can delete post" , "can ban user" , and so on. Write a method 
# called show_privileges() that lists the administrator’s set of privileges. 
# Create an instance of Admin , and call your method.

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
        self.privilidges = []

    def show_privilidges(self):
        print("Privilidges:")
        for i in self.privilidges:
            print(f"- {i}")


admin_user = Admin("Admin", "User", 33, "Everywhere")
admin_user.privilidges = ["can add post", "can delete post" , "can ban user"]
admin_user.show_privilidges()
print("Login attempts:", admin_user.login_attempts)