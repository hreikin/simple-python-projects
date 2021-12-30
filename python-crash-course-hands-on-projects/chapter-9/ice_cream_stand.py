# An ice cream stand is a specific kind of restaurant. Write a class called 
# IceCreamStand that inherits from the Restaurant class you wrote in 
# "restaurant.py" or "three_restaurants.py". Either version of the class will 
# work; just pick the one you like better. Add an attribute called flavors that 
# stores a list of ice cream flavors. Write a method that displays these flavors. 
# Create an instance of IceCreamStand , and call this method.

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}.")
        print(f"Cuisine type: {self.cuisine_type}.")

    def open_restaurant(self):
        print("The restaurant is open.")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, *flavours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours

    def show_flavours(self):
        print("Flavours available:")
        for i in self.flavours:
            print(f"- {i}")


my_ice_cream_stand = IceCreamStand("Ice Cream Stand Name", "Ice Cream", "Strawberry", "Chocolate", "Mint")
my_ice_cream_stand.show_flavours()