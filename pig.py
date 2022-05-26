import pygame


class Pig:
    """Creates pig."""
    def __init__(self, screen):
        """Initialization of the pig and it's started position."""
        self.screen = screen

        # Loading of pig image and getting rectangle.
        self.image = pygame.image.load('images/pig_1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Every new pig appears at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        """Drawn the pig at the current position."""
        self.screen.blit(self.image, self.rect)
