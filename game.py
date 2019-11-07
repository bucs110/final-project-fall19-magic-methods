from main import pygame
from main import character
from main import spriteSheet

class Game:
    def __init__(self,player,sprite_sheet_file):
        self.windowSurface = pygame.display.set_mode((512,384))
        pygame.display.set_caption("Professor Moore's Nightmare")
        self.sprite_sheet = spriteSheet.SpriteSheet(sprite_sheet_file,self.windowSurface)
        self.sprites = self.getSprites()
        self.speed = 4
        self.score = 0
        self.font = pygame.font.SysFont("verdana.ttf",30)
        self.clock = pygame.time.Clock()
        self.player = player
        # change to dictionaries
        self.board = [
            [self.sprite_sheet.packSprite("sky",i*64,0) for i in range(8)],
            [self.sprite_sheet.packSprite("sky",i*64,64) for i in range(8)],
            [self.sprite_sheet.packSprite("sky",i*64,128) for i in range(8)],
            [self.sprite_sheet.packSprite("brick",i*64,192) for i in range(9)],
            [self.sprite_sheet.packSprite("brick",i*64,256) for i in range(9)],
            [self.sprite_sheet.packSprite("brick",i*64,320) for i in range(9)],
        ]

    def getSprites(self):
        sprites = {
            "sky":[self.sprite_sheet.getSprite(32 * i,0,32,32) for i in range(6)],
            "brick":self.sprite_sheet.getSprite(32 * 3,64,32,32) #change pos in sheet
        }
        sprites["sky"] = [pygame.transform.scale2x(sprite) for sprite in sprites["sky"]]
        sprites["brick"] = pygame.transform.scale2x(sprites["brick"])
        return sprites

    def getScore(self):
        text = self.font.render(f'score: {self.score}', True, (255,255,255))
        return text

    def update(self):
        if self.board[3][0]["pos"]["x"] == -64:
            for y in range(3):
                self.board[3+y].pop(0)
                self.board[3+y].append(self.sprite_sheet.packSprite("brick",512,192 + (64*y)))

        for y in range(3):
            for el in self.board[3+y]:
                el["pos"]["x"] -= self.speed

        self.score += 1
        self.clock.tick(30)

    def render(self):
        self.windowSurface.fill((0,0,0))
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x]["type"] == "sky":
                    self.windowSurface.blit(
                        self.sprites[self.board[y][x]["type"]][y],
                        (
                            self.board[y][x]["pos"]["x"],
                            self.board[y][x]["pos"]["y"]
                        )
                    )
                else:
                    self.windowSurface.blit(
                        self.sprites[self.board[y][x]["type"]],
                        (
                            self.board[y][x]["pos"]["x"],
                            self.board[y][x]["pos"]["y"]
                        )
                    )
        self.player.animObj.blit(self.windowSurface,(self.player.X,self.player.y))
        self.windowSurface.blit(self.getScore(),(10,10))

        pygame.display.update()
