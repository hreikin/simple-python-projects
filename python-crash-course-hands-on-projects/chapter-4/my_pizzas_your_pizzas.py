# Start with your program "pizzas.py" from . Make a copy of the list of pizzas, 
# and call it friend_pizzas .
# 
# Then, do the following:
# 
# Add a new pizza to the original list.
# 
# Add a different pizza to the list friend_pizzas .
# 
# Prove that you have two separate lists. Print the message, "My favorite pizzas 
# are:", and then use a for loop to print the first list. Print the message, 
# "My friend’s favorite pizzas are:", and then use a for loop to print the 
# second list. Make sure each new pizza is stored in the appropriate list.

my_pizzas = ["Pepperoni", "Margherita", "Chicken"]
friends_pizzas = my_pizzas[:]

for i in my_pizzas:
    print(f"I like {i} pizza.")
    
print(f"""
I like {my_pizzas[0]} pizza.
I really like {my_pizzas[1]} pizza.
I really, really like {my_pizzas[2]} pizza.
I really love pizza.
""")

my_pizzas.append("BBQ")
friends_pizzas.append("Beef")

print("My favorite pizzas are:")
for i in my_pizzas:
    print(i)

print("My friends favorite pizzas are:")
for i in friends_pizzas:
    print(i)