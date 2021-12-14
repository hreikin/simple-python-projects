def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print("The even number is now: ", number)
        elif number % 2 == 1:
            number = 3* number + 1
            print("The odd number is now: ", number)


number = int(input("Enter a number: "))
collatz(number)