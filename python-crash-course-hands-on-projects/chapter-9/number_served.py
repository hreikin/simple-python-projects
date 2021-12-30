# Start with your program from "restaurant.py". Add an attribute called 
# number_served with a default value of 0. Create an instance called restaurant 
# from this class. Print the number of customers the restaurant has served, and 
# then change this value and print it again. 
# 
# Add a method called set_number_served() that lets you set the number of 
# customers that have been served. Call this method with a new number and print 
# the value again.
#
# Add a method called increment_number_served() that lets you increment the 
# number of customers who’ve been served. Call this method with any number you 
# like that could represent how many customers were served in, say, a day of 
# business.

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}.")
        print(f"Cuisine type: {self.cuisine_type}.")

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self, set_served):
        self.number_served = set_served

    def increment_number_served(self, increment_served):
        self.number_served += increment_served


restaurant = Restaurant("Wah Mans", "Chinese")

print(restaurant.number_served)
restaurant.number_served += 1
print(restaurant.number_served)
restaurant.set_number_served(5)
print(restaurant.number_served)
restaurant.increment_number_served(110)
print(restaurant.number_served)