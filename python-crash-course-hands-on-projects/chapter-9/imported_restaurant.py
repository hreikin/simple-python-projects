# Using your latest Restaurant class, store it in a module. Make a separate file 
# that imports Restaurant . Make a Restaurant instance, and call one of 
# Restaurant’s methods to show that the import statement is working properly.

import imported_restaurant_module

instance = imported_restaurant_module.Restaurant("Wah Mans", "Chinese")

instance.describe_restaurant()