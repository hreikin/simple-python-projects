# Modify the make_shirt() function in "t_shirt.py" so that shirts are large by 
# default with a message that reads I love Python. Make a large shirt and a 
# medium shirt with the default message, and a shirt of any size with a 
# different message.

def make_shirt(size = "Large", message = "I love Python!"):
    print(f"The shirt is  size: {size} \nThe shirt has this message: '{message}'.")

make_shirt()
make_shirt(size = "Medium")
make_shirt(size = "Small", message = "Hello world!")