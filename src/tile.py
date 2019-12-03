import pygame
from src import spriteSheet

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.setpos(x, y)

    def setpos(self, x=0, y=0):
        self.rect.x, self.rect.y = x, y

    def offset(self, x=0, y=0):
        self.rect.move_ip(x, y)
