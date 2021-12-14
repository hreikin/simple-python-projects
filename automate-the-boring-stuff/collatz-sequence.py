# Write a function named collatz() that has one parameter named number . If
# number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1 .
# Then write a program that lets the user type in an integer and that keeps
# calling collatz() on that number until the function returns the value 1 .

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