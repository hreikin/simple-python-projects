# Turn your if - else chain from alien_colours_b into an if - elif - else chain.
# 
# If the alien is green, print a message that the player earned 5 points.
# 
# If the alien is yellow, print a message that the player earned 10 points.
# 
# If the alien is red, print a message that the player earned 15 points.
# 
# Write three versions of this program, making sure each message is printed for 
# the appropriate color alien.

alien_colour = "green"

if alien_colour == "green":
    print("You just earned 5 points.")
elif alien_colour == "yellow":
    print("You just earned 10 points.")
else:
    print("You just earned 15 points.")

alien_colour = "yellow"

if alien_colour == "green":
    print("You just earned 5 points.")
elif alien_colour == "yellow":
    print("You just earned 10 points.")
else:
    print("You just earned 15 points.")

alien_colour = "red"

if alien_colour == "green":
    print("You just earned 5 points.")
elif alien_colour == "yellow":
    print("You just earned 10 points.")
else:
    print("You just earned 15 points.")