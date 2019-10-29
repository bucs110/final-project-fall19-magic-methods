from main import pygame

class SpriteSheet:
    def __init__(self,img_file,video_mode):
        self.sprite_sheet = pygame.image.load(img_file).convert()

    def getSprite(self,x,y,width,height):
        sprite = pygame.Surface((width,height)).convert()
        sprite.blit(self.sprite_sheet,(0,0),(x,y,width,height))
        return sprite

    def packSprite(self,sprite_type,x=0,y=0):
        return {
            "type":sprite_type,
            "pos":
                {
                    "x":x,
                    "y":y
                }
            }
