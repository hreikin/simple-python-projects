# The module random contains functions that generate random numbers in a variety 
# of ways. The function randint() returns an integer in the range you provide. 
# The following code returns a number between 1 and 6:
#
# from random import randint
# x = randint(1, 6)
#
# Make a class Die with one attribute called sides , which has a default value 
# of 6. Write a method called roll_die() that prints a random number between 1 
# and the number of sides the die has. Make a 6-sided die and roll it 10 times. 
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.
from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(x)

six_sides = Die(6)
six_sides.roll_die()

ten_sides = Die(10)
ten_sides.roll_die()

twenty_sides = Die(20)
twenty_sides.roll_die()