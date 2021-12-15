# Create a magic 8-ball program that tells the user to ask the magic 8-ball a 
# question and then returns an answer from a pre-defined list.

import random

# List of replies for the magic 8-ball.
messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

# Ask the user for input and then print out the reply. The message is chosen 
# randomly from the list of messages. List indexes start at 0 so the "-1" at 
# the end is required.
input("Ask the magic 8-ball a question:\n\n")
print("\nThe magic 8-ball says:", messages[random.randint(0, len(messages) - 1)])