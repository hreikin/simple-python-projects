# Make a list of your favorite fruits, and then write a series of independent if 
# statements that check for certain fruits in your list.
# 
# Make a list of your three favorite fruits and call it favorite_fruits .
# 
# Write five if statements. Each should check whether a certain kind of fruit is 
# in your list. If the fruit is in your list, the if block should print a 
# statement, such as You really like bananas!

favourite_fruits = ["apple", "banana", "orange"]

if "apple" in favourite_fruits:
    print("You really like apples.")
if "banana" in favourite_fruits:
    print("You really like bananas.")
if "orange" in favourite_fruits:
    print("You really like oranges.")
if "pear" in favourite_fruits:
    print("You really like pears.")
if "watermelon" in favourite_fruits:
    print("You really like watermelons.")

# This could be done in a much shorter space with some user input.
# fruit = input("Enter a fruit: ")
# if fruit in favourite_fruits:
#     print(f"You really like {fruit}'s.")