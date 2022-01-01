import sys

import pygame

def run_game():
    # Initialize the game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    # Set the background colour to grey.
    bg_colour = (50, 50, 50)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(bg_colour)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()