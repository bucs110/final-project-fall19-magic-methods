import pygame, random
from src import screen
from src import spriteSheet
from src import tile
from src import character
from src import item

class GameScreen(screen.Screen):
    def __init__(self, display, player):
        screen.Screen.__init__(self, display)
        self.sprite_sheet = spriteSheet.SpriteSheet().getKEY()
        self.player = player
        self.reset()

    def reset(self):
        self.player.reset()
        self.speed = 4
        self.score = 0
        self.items = pygame.sprite.Group()
        self.ground = pygame.sprite.Group()
        self.sky = pygame.sprite.Group()
        self.buildings = pygame.sprite.Group()

        n_building = tile.Tile(self.sprite_sheet[f"BUILDING{random.randint(0,3)}"])
        n_building.rect.bottomleft = 64 * 8, random.randint(300, 320)
        self.buildings.add(n_building)

        self.clouds = pygame.sprite.Group()

        for y in range(4):
            for x in range(8):
                t = tile.Tile(self.sprite_sheet[f"SKY{y}"], 64 * x, 64 * y)
                self.sky.add(t)

        for y in range(2):
            for x in range(9):
                t = tile.Tile(self.sprite_sheet["CONCRETE"], 64 * x, 64 * (y + 4))
                self.ground.add(t)

    def setSpeed(self, speed):
        self.speed = speed

    def getScore(self):
        return self.score

    def update(self):
        self.score += 10
        self.bg = pygame.sprite.Group(tuple(self.sky,) + tuple(self.clouds) + tuple(self.buildings) + tuple(self.ground,) + tuple(self.items,))

        if random.randint(0,70 - (self.speed * 2)) == 0:
            n_item = item.Item(self.sprite_sheet["GOBLIN"], 0, 0)
            self.items.add(n_item)

        if random.randint(0,50) == 0:
            n_tile = tile.Tile(self.sprite_sheet[f"CLOUD{random.randint(0,1)}"], 64 * 8, random.randint(0,192))
            self.clouds.add(n_tile)

        for t in self.items:
            t.offset(-self.speed,0)

            if t.rect.x <= -64:
                t.kill()

        for t in self.clouds:
            t.offset(-self.speed/4,0)

            if t.rect.x <= -64:
                t.kill()

        for t in self.buildings:
            t.offset(-self.speed/2,0)

            if t.rect.x <= -t.rect.width:
                t.kill()
            elif t.rect.bottomright[0] <= 512 and t.rect.bottomright[0] > 512 - self.speed/2:
                n_building = tile.Tile(self.sprite_sheet[f"BUILDING{random.randint(0,3)}"])
                n_building.rect.bottomleft = 64 * 8, random.randint(300,320)
                self.buildings.add(n_building)


        for t in self.ground:
            t.offset(-self.speed,0)

            if t.rect.x <= -64:
                t.kill()
                n_tile = tile.Tile(self.sprite_sheet["CONCRETE"], 64 * 8 - (-64 - t.rect.x), t.rect.y)
                self.ground.add(n_tile)

        collisions = pygame.sprite.spritecollide(self.player, self.items, False)
        if collisions:
            for t in collisions:
                if self.player.row == t.row:
                    t.kill()
                    self.player.takeDamage()

    def getBg(self):
        return self.bg
