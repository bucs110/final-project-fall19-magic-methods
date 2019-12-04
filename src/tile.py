import pygame
from src import spriteSheet

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x=0, y=0):
        """
        Initializes a sprite's rectangle with an image and a position.
        args: (Tile object) a reference to the object itself (string) image name (int) x and y coordinates
        returns: none
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.setpos(x, y)

    def setpos(self, x=0, y=0):
        """
        Sets position of a sprite's rectangle.
        args: (Tile object) a reference to the object itself (int) x and y coordinates
        returns: none
        """
        self.rect.x, self.rect.y = x, y

    def offset(self, x=0, y=0):
        """
        Moves a sprite's rectangle relative to its current position.
        args: (Tile object) a reference to the object itself (int) x and y coordinates
        returns: none
        """
        self.rect.move_ip(x, y)
