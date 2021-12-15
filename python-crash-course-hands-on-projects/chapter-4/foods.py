# All versions of the examples in this section of the PDF have avoided using
# for loops when printing to save space. Choose a version of foods.py, and write 
# two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append("cannoli")
friends_foods.append("ice cream")

print("My foods are:")
for i in my_foods:
    print(i)

print("My friends foods are:")
for i in friends_foods:
    print(i)