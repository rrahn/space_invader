
class BulletSettings():
    """A class to store all settings for bullets."""

    def __init__(self):
        """Initialize the bullet's settings."""
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

class ShipSettings():
    """A class to store all settings for the ship."""

    def __init__(self):
        """Initialize the ship's settings."""
        self.ship_speed_factor = 1.5

class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_settings = ShipSettings()

        # Bullet settings
        self.bullet_settings = BulletSettings()
