import pygame, random
from src import tile

class Item(tile.Tile):
    def __init__(self,image, x, y):
        tile.Tile.__init__(self, image, x, y)
        self.row = random.randint(1,3)
        self.setpos(516, 266 + (self.row - 2) * 42)
