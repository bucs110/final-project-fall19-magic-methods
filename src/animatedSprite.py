import pygame
import pyganim


class AnimatedSprite:
    def __init__(self, img_file, x, y, width, height, frames, frameLength):
        """
        Initializes AnimatedSprite Object
        args: self (AnimatedSprite Object) a reference to the object itself
            img_file (string) a path to an image
            x (int) top coordinate of a surface
            y (int) left coordinate of a surface
            width (int) width of a surface
            height (int) height of a surface
            frames (int) the number of frames for the animation
            frameLength (int) the amount of times each frame plays in milisecond
        return: None
        """
        self.rects = [(i * width + x, y, width, height) for i in range(frames)]
        self.images = pyganim.getImagesFromSpriteSheet(img_file, rects=self.rects)
        self.frames = list(zip(self.images, [frameLength] * len(self.images)))
        self.animObj = pyganim.PygAnimation(self.frames)

    def getAnimatedSprite(self):
        """
        Gets the animated objects from the img_file
        args: self (AnimatedSprite Object) a reference to the object itself
        return: (pyganim.PygAnimation) self.animObj
        """
        return self.animObj
