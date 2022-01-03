import sys

import pygame

from settings import Settings

class AlienInvasion():
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()

        # Instantiate the Settings class.
        self.settings = Settings()

        # Set the screen size and window title.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop and set the 
            # background colour from settings.py.
            self.screen.fill(self.settings.bg_colour)

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == "__main__":
    # Make an instance of the class and run the game.
    ai = AlienInvasion()
    ai.run_game()