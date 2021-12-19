# Using the list sandwich_orders from "deli.py", make sure the sandwich 
# 'pastrami' appears in the list at least three times. Add code near the 
# beginning of your program to print a message saying the deli has run out of 
# pastrami, and then use a while loop to remove all occurrences of 'pastrami' 
# from sandwich_orders . Make sure no pastrami sandwiches end up in 
# finished_sandwiches.

sandwich_orders = ["cheese","pastrami", "ham","pastrami", "tuna", "pastrami"]
finished_sandwiches = []

print("We have no pastrami, sorry.")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == "pastrami":
        continue
    else:
        print(f"I made your {current_sandwich} sandwich.")
        finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print(f"The {sandwich} sandwich is finished.")