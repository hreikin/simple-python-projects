# Start with your class from "restaurant.py". Create three different instances 
# from the class, and call describe_restaurant() for each instance.

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}.")
        print(f"Cuisine type: {self.cuisine_type}.")

    def open_restaurant(self):
        print("The restaurant is open.")

restaurant_one = Restaurant("Wah Mans", "Chinese")
restaurant_two = Restaurant("Davians", "Fish & Chips")
restaurant_three = Restaurant("Ghandis", "Indian")

restaurant_one.describe_restaurant()
restaurant_two.describe_restaurant()
restaurant_three.describe_restaurant()