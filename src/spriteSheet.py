import pygame

class SpriteSheet:
    def __init__(self):
        """
        Initializes a dictionary containing sprite surfaces as an instance variable.
        args: (SpriteSheet object) a reference to the object itself
        returns: none
        """
        self.KEY = {
            "SKY0":pygame.image.load("assets/imgs/sky0.png").convert_alpha(),
            "SKY1":pygame.image.load("assets/imgs/sky1.png").convert_alpha(),
            "SKY2":pygame.image.load("assets/imgs/sky2.png").convert_alpha(),
            "SKY3":pygame.image.load("assets/imgs/sky3.png").convert_alpha(),
            "SKY4":pygame.image.load("assets/imgs/sky4.png").convert_alpha(),
            "CLOUD0":pygame.image.load("assets/imgs/cloud0.png").convert_alpha(),
            "CLOUD1":pygame.image.load("assets/imgs/cloud1.png").convert_alpha(),
            "BRICK":pygame.image.load("assets/imgs/brick.png").convert_alpha(),
            "CONCRETE":pygame.image.load("assets/imgs/concrete.png").convert_alpha(),
            "WHISKEY":pygame.image.load("assets/imgs/whiskey.png").convert_alpha(),
            "GOBLIN":pygame.image.load("assets/imgs/goblin.png").convert_alpha(),
            "HEART":pygame.image.load("assets/imgs/heart.png").convert_alpha(),
            "BUILDING0":pygame.image.load("assets/imgs/building0.png").convert_alpha(),
            "BUILDING1":pygame.image.load("assets/imgs/building1.png").convert_alpha(),
            "BUILDING2":pygame.image.load("assets/imgs/building2.png").convert_alpha(),
            "BUILDING3":pygame.image.load("assets/imgs/building3.png").convert_alpha(),
        }

    def getKEY(self):
        """
        Gets the self.key sprite group.
        args: (SpriteSheet object) a reference to the object itself
        returns: (pygame.sprite.Group) key sprite group
        """
        return self.KEY
