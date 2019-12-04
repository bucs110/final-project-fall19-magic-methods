import pygame

class Screen:
    def __init__(self, display, image=None):
        """
        Loads the background image if there is one.
        args: display and (string) image name
        returns: none
        """
        if not image == None:
            self.bg = pygame.image.load(image)
        self.display = display

    def getBg(self):
        """
        Gets the background of the screen.
        args: none
        returns: (pygame.sprite.Group) background sprite group
        """
        return self.bg
