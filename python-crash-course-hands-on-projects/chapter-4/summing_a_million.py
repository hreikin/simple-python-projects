# Make a list of the numbers from one to one million, and then use min() and 
# max() to make sure your list actually starts at one and ends at one million. 
# Also, use the sum() function to see how quickly Python can add a million 
# numbers.

one_million = list(range(1, 1000001))

print(min(one_million))
print(max(one_million))
print(sum(one_million))