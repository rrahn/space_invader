import sys
import pygame

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

    while True:
        gf.check_events(ship)
        ship.update()

        gf.update_screen(screen, si_settings, ship)

if __name__ == "__main__":
    run_app()
