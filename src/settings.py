from dataclasses import dataclass

@dataclass
class BulletSettings():
    """A class to store all settings for bullets."""
    bullet_speed_factor = 1
    bullet_width = 3
    bullet_height = 15
    bullet_color = 60, 60, 60
    bullets_allowed = 3

@dataclass
class ShipSettings():
    """A class to store all settings for the ship."""

    ship_speed_factor = 1.5

@dataclass
class Settings():
    """A class to store all settings for Alien Invasion."""

    # Screen settings
    screen_width = 1200
    screen_height = 800
    bg_color = (230, 230, 230)

    # Ship settings
    ship_settings = ShipSettings()

    # Bullet settings
    bullet_settings = BulletSettings()
