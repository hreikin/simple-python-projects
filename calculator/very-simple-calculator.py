# A very simple CLI based calculator which can perform basic arithmetic operations like 
# addition, subtraction, multiplication or division depending upon the user input.
# The user chooses one of four available options; addition, subtraction, multiplication and division.
# Two numbers are taken as inputs and then if/elif/else branching is used to 
# execute the selected operation using functions.

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

# TO DO: Add a while loop with an option to quit or re-run the program.
# running = True

select = int(input("Select which operation you would like to execute:\n" \
    "1. Addition\n" \
    "2. Subtraction\n" \
    "3. Multiplication\n" \
    "4. Division\n"))

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if select == 1:
    print(first_number, "+", second_number, "=", add(first_number, second_number))
elif select == 2:
    print(first_number, "-", second_number, "=", subtract(first_number, second_number))
elif select == 3:
    print(first_number, "*", second_number, "=", multiply(first_number, second_number))
elif select == 4:
    print(first_number, "/", second_number, "=", divide(first_number, second_number))
else:
    print("Error, invalid input.")