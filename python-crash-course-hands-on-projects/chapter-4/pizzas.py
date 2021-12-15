# Think of at least three kinds of your favorite pizza. Store these pizza names 
# in a list, and then use a for loop to print the name of each pizza.
# 
# Modify your for loop to print a sentence using the name of the pizza instead 
# of printing just the name of the pizza. For each pizza you should have one 
# line of output containing a simple statement like I like pepperoni pizza.
# 
# Add a line at the end of your program, outside the for loop, that states how 
# much you like pizza. The output should consist of three or more lines about 
# the kinds of pizza you like and then an additional sentence, such as I really 
# love pizza!

pizzas = ["Pepperoni", "Margherita", "Chicken"]

def pizzas_a():
    print("\nPizzas A")
    for i in pizzas:
        print(i)

def pizzas_b():
    print("\nPizzas B")
    for i in pizzas:
        print(f"I like {i} pizza.")

def pizzas_c():
    print("\nPizzas C")
    for i in pizzas:
        print(f"I like {i} pizza.")
    print(f"""
    I like {pizzas[0]} pizza.
    I really like {pizzas[1]} pizza.
    I really, really like {pizzas[2]} pizza.
    I really love pizza.
    """)

pizzas_a()
pizzas_b()
pizzas_c()