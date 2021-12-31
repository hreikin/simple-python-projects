# Make two files, cats.txt and dogs.txt. Store at least three names of cats in 
# the first file and three names of dogs in the second file. Write a program 
# that tries to read these files and print the contents of the file to the 
# screen. Wrap your code in a try-except block to catch the FileNotFound error, 
# and print a friendly message if a file is missing. Move one of the files to a 
# different location on your system, and make sure the code in the except block 
# executes properly.

filenames = ["python-crash-course-hands-on-projects/chapter-10/cats-dogs-files/cats.txt", "python-crash-course-hands-on-projects/chapter-10/cats-dogs-files/dogs.txt"]

for file in filenames:
    print("Reading file: " + file)
    try:
        with open(file) as file_object:
            contents = file_object.read()
            print(contents)
    except FileNotFoundError:
        print("Sorry, that file does not exist.")