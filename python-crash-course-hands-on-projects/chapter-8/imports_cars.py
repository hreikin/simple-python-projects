# Using a program you wrote that has one function in it, store that function in 
# a separate file. Import the function into your main program file, and call the 
# function using each of these approaches:
# 
# import module_name
# 
# from module_name import function_name
# 
# from module_name import function_name as fn
# 
# import module_name as mn
# 
# from module_name import *

import imports_cars_functions

car = imports_cars_functions.make_car("Ford1", "Escort1")

for k, v in car.items():
    print(k + ":", v)

from imports_cars_functions import make_car

car = make_car("Ford2", "Escort2")

for k, v in car.items():
    print(k + ":", v)

from imports_cars_functions import make_car as fn

car = fn("Ford3", "Escort3")

for k, v in car.items():
    print(k + ":", v)

import imports_cars_functions as mn

car = mn.make_car("Ford4", "Escort4")

for k, v in car.items():
    print(k + ":", v)

from imports_cars_functions import *

car = make_car("Ford5", "Escort5")

for k, v in car.items():
    print(k + ":", v)