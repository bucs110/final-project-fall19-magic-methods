import pygame, random
from src import tile

class Item(tile.Tile):
    def __init__(self,image, x, y):
        """
        Generates tiles with an image and x and y position.
        args: (Item object) a reference to the object itself (string) image name (int) x and y coordinates
        returns: none
        """
        tile.Tile.__init__(self, image, x, y)
        self.row = random.randint(1,3)
        self.setpos(516, 266 + (self.row - 2) * 42)
