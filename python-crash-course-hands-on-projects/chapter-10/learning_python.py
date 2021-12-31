# Open a blank file in your text editor and write a few lines summarizing what 
# you’ve learned about Python so far. Start each line with the phrase In Python 
# you can.... Save the file as learning_python.txt in the same directory as your 
# exercises from this chapter. Write a program that reads the file and prints 
# what you wrote three times. Print the contents once by reading in the entire 
# file, once by looping over the file object, and once by storing the lines in a 
# list and then working with them outside the with block.

with open("python-crash-course-hands-on-projects/chapter-10/learning_python.txt") as file_object:
    contents = file_object.read()
    print(contents)

with open("python-crash-course-hands-on-projects/chapter-10/learning_python.txt") as file_object:
    for line in file_object:
        print(line)

with open("python-crash-course-hands-on-projects/chapter-10/learning_python.txt") as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)