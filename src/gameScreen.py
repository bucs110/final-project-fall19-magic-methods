import pygame, random
from src import screen
from src import spriteSheet
from src import tile
from src import character
from src import item

class GameScreen:
    def __init__(self, display, player):
        screen.Screen.__init__(self, display)
        self.sprite_sheet = spriteSheet.SpriteSheet("assets/temp_sprite.png").getKEY()
        self.speed = 2
        self.score = 0
        self.items = pygame.sprite.Group()
        self.ground = pygame.sprite.Group()
        self.sky = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()
        self.player = player

        for y in range(4):
            for x in range(8):
                t = tile.Tile(self.sprite_sheet[f"sky{4-y}"], 64 * x, 64 * y)
                self.sky.add(t)

        for y in range(2):
            for x in range(9):
                t = tile.Tile(self.sprite_sheet["ground"], 64 * x, 64 * (y + 4))
                self.ground.add(t)

    def setSpeed(self, speed):
        self.speed = speed

    def getScore(self):
        return self.score

    def update(self):
        self.score += 10
        self.bg = pygame.sprite.Group(tuple(self.ground,) + tuple(self.sky,) + tuple(self.clouds,) + tuple(self.items,))

        if random.randint(0,100) == 0:
            n_item = item.Item(self.sprite_sheet["whiskey"], 0, 0)
            self.items.add(n_item)

        if random.randint(0,50) == 0:
            n_tile = tile.Tile(self.sprite_sheet[f"cloud{random.randint(0,1)}"], 64 * 8, random.randint(0,192))
            self.clouds.add(n_tile)

        for t in self.items:
            t.offset(-self.speed,0)

            if t.rect.x <= -64:
                t.kill()

        for t in self.clouds:
            t.offset(-self.speed/2,0)

            if t.rect.x <= -64:
                t.kill()

        for t in self.ground:
            t.offset(-self.speed,0)

            if t.rect.x <= -64:
                t.kill()
                n_tile = tile.Tile(self.sprite_sheet["ground"], 64 * 8 - (-64 - t.rect.x), t.rect.y)
                self.ground.add(n_tile)

        collisions = pygame.sprite.spritecollide(self.player, self.items, False)
        if collisions:
            for t in collisions:
                if self.player.row == t.row:
                    t.kill()
                    self.player.takeDamage()

    def getBg(self):
        return self.bg
