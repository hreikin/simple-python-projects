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
file_content = input("Please write your note now and hit ENTER to save: ")

# Create the file.
def open_directory(path):
    """Open directory for writing, creating any parent directories as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, "w")

with open_directory(save_location + file_name + file_extension) as file:

    file.write(file_content)
    file.close()

# Show the saved files location and "file_content".
print(f"The file was saved to: \"{save_location}{file_name}{file_extension}\"")

# The files content could be displayed using the line below but i would like to include 
# multi-line note taking if possible. The code block below opens the file and reads it 
# line by line.

# print(f"The files content was:\n\n{file_content}")

print("The files content was:\n")

file = open(save_location + file_name + file_extension)

while True:
    line = file.readline()

    if len(line) == 0:
        break

    print(line, end="")

file.close()

print("\n\nGoodbye!")