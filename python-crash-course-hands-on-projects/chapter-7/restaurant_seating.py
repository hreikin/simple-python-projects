# Write a program that asks the user how many people are in their dinner group. 
# If the answer is more than eight, print a message saying they’ll have to wait 
# for a table. Otherwise, report that their table is ready.

seats_required = input("How many people are in your dinner group ? ")
seats_required = int(seats_required)

if seats_required > 8:
    print("Sorry, you will need to wait for a table.")
else:
    print("Your table is ready.")