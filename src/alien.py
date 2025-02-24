import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, settings, screen):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Load and scale the alien image
        self.image = pygame.image.load('images/Space-invaders-top-alien.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Capture the alien's exact position
        self.x = float(self.rect.x)

    def draw(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
