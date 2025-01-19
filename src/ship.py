import pygame

class Ship():

    def __init__(self, screen, settings):
        """Initialize the ship and set its starting position"""
        self.screen = screen
        self.settings = settings.ship_settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/64px-Space-Invaders-ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Movement flag
        self.moving_right = False
        self.moving_left = False

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor

        self.rect.centerx = self.center

    def draw(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx
