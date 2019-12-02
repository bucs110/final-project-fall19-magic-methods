import pygame

class SpriteSheet:
    def __init__(self,img_file):
        self.sprite_sheet = pygame.image.load(img_file).convert_alpha()
        self.KEY = {
            "sky0":self.getSprite(256, 0, 64, 64),
            "sky1":self.getSprite(192, 0, 64, 64),
            "sky2":self.getSprite(128, 0, 64, 64),
            "sky3":self.getSprite(64, 0, 64, 64),
            "sky4":self.getSprite(0, 0, 64, 64),
            "ground":self.getSprite(320, 0, 64, 64),
            "cloud0":self.getSprite(0, 64, 128, 64),
            "cloud1":self.getSprite(128, 64, 64, 64),
            "whiskey":self.getSprite(192, 64, 64, 64)
        }

    def getSprite(self,x,y,width,height):
        sprite = pygame.Surface((width,height))
        sprite.set_colorkey((100,100,100))
        sprite.blit(self.sprite_sheet,(0,0),(x,y,width,height))
        return sprite

    def getKEY(self):
        return self.KEY
