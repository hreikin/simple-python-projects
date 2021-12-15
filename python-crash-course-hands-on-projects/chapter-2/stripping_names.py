# Store a person’s name, and include some whitespace characters at the beginning 
# and end of the name. Make sure you use each character combination, "\t" and 
# "\n" , at least once. Print the name once, so the whitespace around the name 
# is displayed. Then print the name using each of the three stripping functions, 
# lstrip() , rstrip() , and strip() .

name = "\n\n\threikin\t\n"
print(f"Name with whitespace: {name}")
print("Using \"lstrip()\" the name is:", name.lstrip())
print("Using \"rstrip()\" the name is:", name.rstrip())
print("Using \"strip()\" the name is:", name.strip())