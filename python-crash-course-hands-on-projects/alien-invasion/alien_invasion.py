import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings and the screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create the player ship.
    ship = Ship(screen)

    # Start the main loop for the game.
    while True:

        # Call check_events function to watch for keyboard and mouse events.
        gf.check_events(ship)

        # Call update_screen function to update the images and flip to the new 
        # screen.
        gf.update_screen(ai_settings, screen, ship)

run_game()