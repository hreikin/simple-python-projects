# Write a function named collatz() that has one parameter named number . If
# number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1 .
# Then write a program that lets the user type in an integer and that keeps
# calling collatz() on that number until the function returns the value 1 .

# Add try and except statements to the project to detect whether the
# user types in a noninteger string. Normally, the int() function will raise a
# ValueError error if it is passed a noninteger string. In the except clause, 
# print a message to the user saying they must enter an integer.

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print("The even number is now: ", number)
        elif number % 2 == 1:
            number = 3* number + 1
            print("The odd number is now: ", number)

try:
    number = int(input("Enter a number: "))
    collatz(number)
except ValueError:
    print("Please enter an integer value.")