import pygame
from pygame.sprite import Group

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
    ship = Ship(ai_settings, screen)

    # Make a group to store the bullets in.
    bullets = Group()

    # Start the main loop for the game.
    while True:

        # Call check_events function to watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)

        # Update the player ships position in response to input and ensures the 
        # updated position is used when drawing to the screen.
        ship.update()

        # Calls update() for each bullet in the group.
        gf.update_bullets()

        # Call update_screen function to update the images and flip to the new 
        # screen.
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()