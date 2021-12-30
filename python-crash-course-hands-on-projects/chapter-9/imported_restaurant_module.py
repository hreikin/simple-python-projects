# Using your latest Restaurant class, store it in a module. Make a separate file 
# that imports Restaurant . Make a Restaurant instance, and call one of 
# Restaurant’s methods to show that the import statement is working properly.

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