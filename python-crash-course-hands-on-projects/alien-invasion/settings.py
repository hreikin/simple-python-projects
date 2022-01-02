class Settings():
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        
        # Screen related settings.
        self.screen_width = 1200
        self.screen_height = 800
        
        # Set the background colour to an off white.
        self.bg_colour = (230, 230, 230)

        # Ship settings.
        self.ship_speed_factor = 1.5

        # Bullet settings.
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.bullets_allowed = 3