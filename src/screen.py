import pygame

class Screen:
    def __init__(self, display, image=None):
        if not image == None:
            self.bg = pygame.image.load(image)

    def getBg(self):
        return self.bg
