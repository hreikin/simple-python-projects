# A Python dictionary can be used to model an actual dictionary. However, to 
# avoid confusion, let’s call it a glossary.
# 
# Think of five programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary, and store their meanings as 
# values.
# 
# Print each word and its meaning as neatly formatted output. You might print 
# the word followed by a colon and then its meaning, or print the word on one 
# line and then print its meaning indented on a second line. Use the newline 
# character ( \n ) to insert a blank line between each word-meaning pair in your 
# output.

glossary = {
            "List": "Lists are used to store multiple items in a single variable. Lists are created using square brackets.",
            "Tuple": "Tuples are used to store multiple items in a single variable. A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.",
            "Dictionary": "Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered, changeable and do not allow duplicates. Dictionaries are written with curly brackets, and have keys and values.",
            "String": "Strings in python are surrounded by either single quotation marks, or double quotation marks.",
            "Integer": "Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length."
            }

for k, v in glossary.items():
    print("\n" + k + ":", v)