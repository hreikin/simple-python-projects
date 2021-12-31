# One common problem when prompting for numerical input occurs when people 
# provide text instead of numbers. When you try to convert the input to an int, 
# you’ll get a TypeError . Write a program that prompts fo two numbers. Add them 
# together and print the result. Catch the TypeError if either input value is 
# not a number, and print a friendly error message. Test your program by 
# entering two numbers and then by entering some text instead of a number.

print("Enter two numbers to be added together.")

first_number = input("First number: ")
second_number = input("Second number: ")
try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("Numbers only please.")
else:
    print(answer)