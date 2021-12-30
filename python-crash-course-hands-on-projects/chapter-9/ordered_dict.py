# Start with "glossary.py"", where you used a standard dictionary to represent a 
# glossary. Rewrite the program using the OrderedDict class and make sure the 
# order of the output matches the order in which key-value pairs were added to 
# the dictionary.
from collections import OrderedDict

glossary = OrderedDict()

glossary.update({"List": "Lists are used to store multiple items in a single variable. Lists are created using square brackets."})
glossary.update({"Tuple": "Tuples are used to store multiple items in a single variable. A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets."})
glossary.update({"Dictionary": "Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered, changeable and do not allow duplicates. Dictionaries are written with curly brackets, and have keys and values."})
glossary.update({"String": "Strings in python are surrounded by either single quotation marks, or double quotation marks.",})
glossary.update({"Integer": "Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length."})

for k, v in glossary.items():
    print("\n" + k + ":", v)