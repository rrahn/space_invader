import pygame

from pygame.sprite import Group
from game_stats import GameStats
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
    stats = GameStats(si_settings)
    # Create alien fleet
    gf.create_fleet(si_settings, screen, aliens)

    while True:
        gf.check_events(screen, si_settings, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(si_settings, screen, aliens, bullets)
            gf.update_aliens(si_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(screen, si_settings, ship, aliens, bullets)

if __name__ == "__main__":
    run_app()
