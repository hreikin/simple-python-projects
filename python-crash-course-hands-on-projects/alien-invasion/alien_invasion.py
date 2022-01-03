import sys

import pygame

class AlienInvasion():
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Set the background colour.
        self.bg_colour = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_colour)

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == "__main__":
    # Make an instance of the class and run the game.
    ai = AlienInvasion()
    ai.run_game()