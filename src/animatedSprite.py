import pygame
import pyganim

class AnimatedSprite:
    def __init__(self,img_file,x,y,width,height,frames,frameLength):
        self.rects = [(i * width + x,y,width,height) for i in range(frames)]
        self.images = pyganim.getImagesFromSpriteSheet(img_file,rects=self.rects)
        self.frames = list(zip(self.images, [frameLength] * len(self.images)))
        self.animObj = pyganim.PygAnimation(self.frames)

    def getAnimatedSprite(self):
        return self.animObj