import pygame
from src import spriteSheet

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x=0, y=0):
        """
        Initializes the player's rectangle with an image and a position.
        args: (string) image name (int) x and y coordinates
        returns: none
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.setpos(x, y)

    def setpos(self, x=0, y=0):
        """
        Sets position of the player's rectangle.
        args: (int) x and y coordinates
        returns: none
        """
        self.rect.x, self.rect.y = x, y

    def offset(self, x=0, y=0):
        """
        Moves the player's rectangle in place.
        args: (int) x and y coordinates
        returns: none
        """
        self.rect.move_ip(x, y)
