# Visit Project Gutenberg (http://gutenberg.org/) and find a few texts you’d 
# like to analyze. Download the text files for these works, or copy the raw text 
# from your browser into a text file on your computer. You can use the count() 
# method to find out how many times a word or phrase appears in a string. For 
# example, the following code counts the number of times 'row' appears in a 
# string:
# 
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3
# 
# Notice that converting the string to lowercase using lower() catches all 
# appearances of the word you’re looking for, regardless of how it’s formatted. 
# Write a program that reads the files you found at Project Gutenberg and 
# determines how many times the word 'the' appears in each text.

filenames = [
    "python-crash-course-hands-on-projects/chapter-10/common-words-files/Free-as-in-Freedom.txt", 
    "python-crash-course-hands-on-projects/chapter-10/common-words-files/IBM-1401-Programming-Systems.txt"
    ]

for file in filenames:
    print("Reading file: " + file)
    with open(file) as file_object:
        contents = file_object.read()
        amount = contents.lower().count("the")
        print(f"The word 'the' appears {amount} times.")