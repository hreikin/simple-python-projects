# Think of your favorite mode of transportation, such as a motorcycle or a car, 
# and make a list that stores several examples. Use your list to print a series 
# of statements about these items, such as “I would like to own a Honda 
# motorcycle.”

cars = ["Mercedes", "Ferrari", "Honda", "VW"]
print(f"I would like to own a {cars[0]}.")
print(f"I would like to own a {cars[1]}.")
print(f"I would like to own a {cars[2]}.")
print(f"I would like to own a {cars[3]}.")

for brand in cars:
    print(f"I would like to own a {brand}.")