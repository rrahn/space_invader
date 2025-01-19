import sys
import pygame

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

def update_screen(screen, settings, ship, bullets):
    """
    Update images on the screen and flip to the new screen.
    Args:
        screen (pygame.Surface): The surface on which to draw the game elements.
        settings (Settings): An instance of the Settings class containing game settings.
        ship (Ship): An instance of the Ship class representing the player's ship.
        bullets (pygame.sprite.Group): The group of bullets currently active in the game.
    """
    screen.fill(settings.bg_color)
    [bullet.draw() for bullet in bullets]
    ship.draw()
    pygame.display.flip()

def update_bullets(bullets):
    """
    Update the positions of all bullets and remove bullets that have gone off-screen.
    Args:
        bullets (pygame.sprite.Group): A group of bullet sprites to be updated.
    """
    bullets.update()

    [bullets.remove(bullet) for bullet in bullets.copy() if bullet.rect.bottom <= 0]
