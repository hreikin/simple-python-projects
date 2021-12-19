# Write a program that polls users about their dream vacation. Write a prompt 
# similar to "If you could visit one place in the world, where would you go?" 
# Include a block of code that prints the results of the poll.

users = ["jay", "neil", "morgan"]
results = []

while users:
    current_answer = input("If you could visit one place in the world, where would you go? ")
    users.pop()
    results.append(current_answer)

for current_answer in results:
    print(current_answer)