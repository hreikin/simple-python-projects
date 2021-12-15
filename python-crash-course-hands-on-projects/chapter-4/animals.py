# Think of at least three different animals that have a common characteristic. 
# Store the names of these animals in a list, and then use a for loop to print 
# out the name of each animal.
#
# Modify your program to print a statement about each animal, such as "A dog 
# would make a great pet."
# 
# Add a line at the end of your program stating what these animals have in 
# common. You could print a sentence such as "Any of these animals would make a 
# great pet!"

animals = ["Dog", "Cat", "Rabbit"]

def animals_a():
    print("\nAnimals A")
    for i in animals:
        print(i)

def animals_b():
    print("\nAnimals B")
    for i in animals:
        print(f"A {i} would make a great pet.")

def animals_c():
    print("\nAnimals C")
    for i in animals:
        print(f"A {i} would make a great pet.")
    print("Any of these animals would make a great pet.")

animals_a()
animals_b()
animals_c()