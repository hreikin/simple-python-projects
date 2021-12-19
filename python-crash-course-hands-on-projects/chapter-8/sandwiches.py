# Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the 
# function call provides, and it should print a summary of the sandwich that is 
# being ordered. Call the function three times, using a different number of 
# arguments each time.

def make_sandwich(*items):
    print("\nI'll make you a great sandwich:")
    for item in items:
        print(".....adding " + item + " to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')