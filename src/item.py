import pygame, random
from src import tile

class Item(tile.Tile):
    def __init__(self,img_file, x, y, width, height):
        tile.Tile.__init__(img_file, x, y, width, height)
        self.row = random.randint(1,3)
        self.move(516, 256 + (self.row - 2) * 42)
