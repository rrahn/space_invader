import sys
import pygame

def on_press_key(event, ship):
    """Respond to key releases by updating the ship's movement flags.
    Args:
        event (pygame.event): The event object containing information about the key release.
        ship (Ship): The ship object whose movement flags are to be updated.
    """
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True

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

def check_events(ship):
    """
    Respond to keypresses and mouse events.
    Parameters:
        ship (Ship): The ship object to control based on user input.
    Handles:
        - QUIT event to exit the game.
        - KEYDOWN event to handle key press actions.
        - KEYUP event to handle key release actions.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            on_press_key(event, ship)
        elif event.type == pygame.KEYUP:
            on_release_key(event, ship)

def update_screen(screen, settings, ship):
    """
    Update images on the screen and flip to the new screen.
    Args:
        screen (pygame.Surface): The surface on which to draw the game elements.
        settings (Settings): An instance of the Settings class containing game settings.
        ship (Ship): An instance of the Ship class representing the player's ship.
    """
    screen.fill(settings.bg_color)
    ship.draw()
    pygame.display.flip()
