# Wrap your code from "addition.py" in a while loop so the user can continue 
# entering numbers even if they make a mistake and enter text instead of a 
# number.

while True:
    print("Enter two numbers to be added together.")
    print("Type 'q' to exit.")
    first_number = input("First number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Numbers only please.")
    else:
        print(answer)