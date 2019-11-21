import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,img_file,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = pygame.image.load(img_file)
        tile = pygame.Surface((width,height))
        tile.blit(self.sprite_sheet,(0,0),(x,y,width,height))
        self.image = tile
        self.rect = tile.get_rect()

    def move(self,x,y):
        self.rect.x += x
        self.rect.y += y
