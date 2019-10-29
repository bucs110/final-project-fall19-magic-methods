from main import game
from main import pygame
from main import pyganim

class Character:
    def __init__(self):
        self.X = 40
        self.y = 256
        self.jump_state = False
        self.lives = 3
        # create animatedSprite class
        self.rects = [(i * 32,32,32,32) for i in range(6)]
        self.images = pyganim.getImagesFromSpriteSheet("assets/temp_sprite.png",rects=self.rects)
        self.images = [pygame.transform.scale2x(image) for image in self.images]
        self.frames = list(zip(self.images, [200] * len(self.images)))
        self.animObj = pyganim.PygAnimation(self.frames)
        self.animObj.play()

    def jump(self):
        # check event queue
        self.jump_state = True
        if self.jump_state:
            pygame.time.set_timer(25,400)
            self.y -= 20
