# Add an attribute called login_attempts to your User class from "users.py". 
# Write a method called increment_login_attempts() that increments the value of 
# login_attempts by 1. Write another method called reset_login_attempts() that 
# resets the value of login_attempts to 0.
#
# Make an instance of the User class and call increment_login_attempts() several 
# times. Print the value of login_attempts to make sure it was incremented 
# properly, and then call reset_login_attempts() . Print login_attempts again to 
# make sure it was reset to 0.

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


user1 = User("Michael", "Haslam", 33, "Scotland")

print("Login attempts:", user1.login_attempts)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print("Login attempts:", user1.login_attempts)
user1.reset_login_attempts()
print("Login attempts:", user1.login_attempts)