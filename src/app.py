import sys
import pygame

from alien import Alien
from pygame.sprite import Group
from settings import Settings
from ship import Ship

import game_functions as gf

def run_app():
    """Initialize the screen and run the main game loop"""
    pygame.init()

    si_settings = Settings()
    screen = pygame.display.set_mode((si_settings.screen_width, si_settings.screen_height))
    pygame.display.set_caption("Space Invaders")
    ship = Ship(screen, si_settings)
    # Group of bullets shot by the space ship
    bullets = Group()
    # Group of aliens
    aliens = Group()

    # Create alien
    alien = Alien(si_settings, screen)
    gf.create_fleet(si_settings, screen, aliens)

    while True:
        gf.check_events(screen, si_settings, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(screen, si_settings, ship, aliens, bullets)

if __name__ == "__main__":
    run_app()
