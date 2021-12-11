import os
import platform

running = True
ask_to_retry = True
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
print("\n***Welcome to the note taking app!***")

while running:
    # Display the "save_location" to the user.
    print(f"\nThe current location files will be saved is \"{save_location}\".")

    # Ask the user for a "file_name".
    file_name = input("\nPlease give a name to the note you want to save: ")

    # Ask the user for the "file_content".
    print("""
    Please write your note now and when you have finished press ENTER and then press
    either CTRL+D (Linux/Mac) or CTRL+Z (Windows) to save.
    
    Multiple lines and paragraphs are allowed, to start a new line or paragraph you 
    can press ENTER: 
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
    print(f"\nThe file was saved to: \"{save_location}{file_name}{file_extension}\"")

    # This opens the file and reads it line by line and prints it to the screen before 
    # closing the file.
    print("\nThe files content was:\n")

    file = open(save_location + file_name + file_extension)

    while True:
        line = file.readline()

        if len(line) == 0:
            break

        print(line, end="")

    file.close()

    while ask_to_retry:
        # Ask if the user wants to create another note. If the input is invalid then ask again.
        running = input("\nDo you want to create another note (yes/no) ? ")
        
        # Check the users answer and either restarts the program or exits it.
        if running.lower().startswith("y") or running.upper().startswith("Y"):
                print("\nOk, let's carry on then.")
                ask_to_retry = False
        elif running.lower().startswith("n") or running.upper().startswith("N"):
                print("\nOk, thank you.")
                running = False
                ask_to_retry = False
        else:
            print("***Invalid input, please try again.***")
    else:
        ask_to_retry = True
else:
    print("\nGoodbye!")