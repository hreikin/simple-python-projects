import os
import platform

file_extension = ".txt"

# Check which OS the user has and figure out and join the home drive, path and "save_location" 
# for windows, or just home directory and "save_location" for linux/mac. We use "os.path.join" 
# instead of joining strings to ensure the path has the correct format expected by the users 
# operating system.
if platform.platform().startswith("Windows"):
    save_location = os.path.join(os.getenv("HOMEDRIVE"),
                                os.getenv("HOMEPATH"),
                                "python-notes/")
else:
    save_location = os.path.join(os.getenv("HOME"),
    "python-notes/")

# Print a welcome message.
print("\n***Welcome to the note taking app!***\n")

# Display the "save_location" to the user.
print(f"The current location files will be saved is \"{save_location}\".\n")

# Ask the user for a "file_name".
file_name = input("Please give a name to the note you want to save: ")

# Ask the user for the "file_content".
print("""
Please write your note now and hit CTRL+D (Linux/Mac) or CTRL+Z (Windows) to save.
You can press ENTER to start writing on a new line: 
""")
file_content = []

# This accepts the user input until it receives an EOFError.
while True:
    try:
        line = input()
    except EOFError:
        break

    # This appends each line with a newline character at the end which allows for 
    # multiline input to be saved to the file.
    file_content.append(line + "\n")

# Create the file.
def open_directory(path):
    """Open directory for writing, creating any parent directories as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, "w")

with open_directory(save_location + file_name + file_extension) as file:

    # Use "file.writelines" to write the individual lines to the file as "file.write" 
    # only accepts a string as input.
    file.writelines(file_content)
    file.close()

# Show the saved files location and "file_content".
print(f"The file was saved to: \"{save_location}{file_name}{file_extension}\"")

# This opens the file and reads it line by line and prints it to the screen before 
# closing the file.
print("The files content was:\n")

file = open(save_location + file_name + file_extension)

while True:
    line = file.readline()

    if len(line) == 0:
        break

    print(line, end="")

file.close()

print("\nGoodbye!")