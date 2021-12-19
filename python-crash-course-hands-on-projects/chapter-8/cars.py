# Write a function that stores information about a car in a dictionary. The 
# function should always receive a manufacturer and a model name. It should then 
# accept an arbitrary number of keyword arguments. 
# 
# Call the function with the required information and two other name-value 
# pairs, such as a color or an optional feature. Your function should work for a 
# call like this one:
# 
# car = make_car('subaru', 'outback', color='blue', tow_package=True) 
# 
# Print the dictionary that’s returned to make sure all the information was 
# stored correctly.

def make_car(manufacturer, model, **car_info):

    car = {}
    car["manufacturer"] = manufacturer
    car["model"] = model

    for k, v in car_info.items():
        car[k] = v
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)

for k, v in car.items():
    print(k + ":", v)