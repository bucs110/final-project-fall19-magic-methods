import pygame, random
from src import spriteSheet
from src import item

class Background:
    def __init__(self):
        self.board = []
        self.tiles = pygame.sprite.Group()
        for y in range(4):
            row = []
            for x in range(8):
                t = spriteSheet.SpriteSheet("assets/temp_sprite.png",64 * y, 0, 64, 64)
                t.move(64 * x, y * 64)
                row.append(t)
                self.tiles.add(t)
            self.board.append(row)

        for y in range(2):
            row = []
            for x in range(9):
                t = tile.Tile("assets/temp_sprite.png",64 * 5, 0, 64, 64)
                t.move(64 * x, 64 * (y + 4))
                row.append(t)
                self.tiles.add(t)
            self.board.append(row)

        self.speed = 2

    def update(self):
        for row in self.board[4:]:
            for t in row:
                t.move(-self.speed, 0)

            if row[0].rect.x <= -64:
                row[0].kill()
                row.pop(0)
                n_tile = tile.Tile("assets/temp_sprite.png",64 * 5, 0, 64, 64)
                n_tile.move(64 * 8, row[0].rect.y)
                row.append(n_tile)
                self.tiles.add(n_tile)

            # if random.choice(True,False):
            #     n_item = item.Item("assets/temp_sprite.png",128, 192, 64, 64)
            #     n_item.move(100,100)