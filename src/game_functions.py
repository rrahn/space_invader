import pygame
import sys

from alien import Alien
from bullet import Bullet

def on_press_key(event, screen, settings, ship, bullets):
    """Respond to key releases by updating the ship's movement flags.
    Args:
        event (pygame.event): The event object containing information about the key release.
        screen (pygame.Surface): The surface on which to draw the game elements.
        settings (Settings): An instance of the Settings class containing game settings.
        ship (Ship): The ship object whose movement flags are to be updated.
        bullets (pygame.sprite.Group): The group of bullets currently active in the game.
    """
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(screen, settings.bullet_settings, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(screen, settings, ship, bullets):
    """
    Create a new bullet and add it to the bullets group if the limit is not exceeded.
    Args:
        screen (pygame.Surface): The surface on which to draw the game elements.
        settings (BulletSettings): The bullet settings object containing game settings.
        ship (Ship): The ship object that will fire the bullet.
        bullets (pygame.sprite.Group): The group of bullets currently active in the game.
    """
    if (len(bullets) < settings.bullets_allowed):
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def on_release_key(event, ship):
    """Respond to key releases by updating the ship's movement flags.
    Args:
        event (pygame.event): The event object containing information about the key release.
        ship (Ship): The ship object whose movement flags are to be updated.
    """
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False

def check_events(screen, settings, ship, bullets):
    """
    Respond to keypresses and mouse events.
    Parameters:
        screen (pygame.Surface): The surface on which to draw the game elements.
        settings (Settings): An instance of the Settings class containing game settings.
        ship (Ship): The ship object to control based on user input.
        bullets (pygame.sprite.Group): The group of bullets currently active in the game.
    Handles:
        - QUIT event to exit the game.
        - KEYDOWN event to handle key press actions.
        - KEYUP event to handle key release actions.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            on_press_key(event, screen, settings, ship, bullets)
        elif event.type == pygame.KEYUP:
            on_release_key(event, ship)

def get_number_aliens_x(settings, alien_width):
    """
    Determine the number of aliens that fit in a row.
    Args:
        settings (Settings): An instance of the Settings class containing game settings.
        alien_width (int): The width of an alien in pixels.
    Returns:
        int: The number of aliens that fit in a row.
    """
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(settings, ship_height, alien_height):
    """
    Determine the number of rows of aliens that fit on the screen.
    Args:
        settings (Settings): An instance of the Settings class containing game settings.
        ship_height (int): The height of the ship in pixels.
        alien_height (int): The height of an alien in pixels.
    Returns:
        int: The number of rows of aliens that fit on the screen.
    """
    available_space_y = settings.screen_height - (3 * alien_height) - ship_height
    number_rows = min(int(available_space_y / (2 * alien_height)), 4)
    return number_rows

def create_alien(settings, screen, aliens, alien_number, row_number):
    """
    Create an alien and place it in the row.
    Args:
        settings (Settings): An instance of the Settings class containing game settings.
        screen (pygame.Surface): The surface on which to draw the game elements.
        aliens (pygame.sprite.Group): The group of aliens to be created.
        alien_number (int): The position of the alien in the row.
        row_number (int): The row number in which the alien is placed.
    """
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(settings, screen, aliens):
    """
    Create a fleet of aliens.
    Args:
        settings (Settings): An instance of the Settings class containing game settings.
        screen (pygame.Surface): The surface on which to draw the game elements.
        aliens (pygame.sprite.Group): The group of aliens to be created.
    """
    alien = Alien(settings, screen)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, alien.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens, alien_number, row_number)


def update_screen(screen, settings, ship, aliens, bullets):
    """
    Update images on the screen and flip to the new screen.
    Args:
        screen (pygame.Surface): The surface on which to draw the game elements.
        settings (Settings): An instance of the Settings class containing game settings.
        ship (Ship): An instance of the Ship class representing the player's ship.
        aliens (pygame.sprite.Group): The group of aliens.
        bullets (pygame.sprite.Group): The group of bullets currently active in the game.
    """
    screen.fill(settings.bg_color)
    [bullet.draw() for bullet in bullets]
    ship.draw()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    """
    Update the positions of all bullets and remove bullets that have gone off-screen.
    Args:
        bullets (pygame.sprite.Group): A group of bullet sprites to be updated.
    """
    bullets.update()

    [bullets.remove(bullet) for bullet in bullets.copy() if bullet.rect.bottom <= 0]
