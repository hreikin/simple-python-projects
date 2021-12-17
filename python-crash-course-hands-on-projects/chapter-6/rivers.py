# Make a dictionary containing three major rivers and the country each river 
# runs through. One key-value pair might be 'nile': 'egypt'.
# 
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# 
# Use a loop to print the name of each river included in the dictionary.
# 
# Use a loop to print the name of each country included in the dictionary.

rivers = {"nile" : "egypt", "thames" : "england", "ganges" : "india"}

for k, v in rivers.items():
    print(f"The {k} runs through {v}.")

for k in rivers.keys():
    print(k)

for v in rivers.values():
    print(v)