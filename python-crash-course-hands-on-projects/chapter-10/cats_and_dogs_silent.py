# Modify your except block in "cats_and_dogs.py" to fail silently if either file 
# is missing.

filenames = ["python-crash-course-hands-on-projects/chapter-10/cats-dogs-files/cats.txt", "python-crash-course-hands-on-projects/chapter-10/cats-dogs-files/dogs.txt"]

for file in filenames:
    print("Reading file: " + file)
    try:
        with open(file) as file_object:
            contents = file_object.read()
            print(contents)
    except FileNotFoundError:
        pass