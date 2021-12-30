# Make a class called User. Create two attributes called first_name and last_name 
# and then create several other attributes that are typically stored in a user 
# profile. Make a method called describe_user() that prints a summary of the 
# user’s information. Make another method called greet_user() that prints a 
# personalized greeting to the user. Create several instances representing 
# different users, and call both methods for each user.

class User():
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"""
        Here are the users details:
        Name: {self.first_name} {self.last_name}
        Age: {self.age}
        Location: {self.location}
        """)

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}.")

user1 = User("Michael", "Haslam", 33, "Scotland")
user2 = User("Victoria", "Brown", 36, "Scotland")
user3 = User("Chris", "Haslam", 31, "England")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()