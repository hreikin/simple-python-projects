import sys

import pygame

from settings import Settings
from ship import Ship

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

        # Instantiate the player ship.
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        # Respond to keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        # Redraw the screen, set the background colour and draw the ship.
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == "__main__":
    # Make an instance of the class and run the game.
    ai = AlienInvasion()
    ai.run_game()