import sys
import pygame
from src import character
from src import background
from src import tile

class Controller:
    def __init__(self):
        self.windowSurface = pygame.display.set_mode((512,384))
        self.bg = background.Background(self.windowSurface)
        icon = pygame.image.load("assets/SAM.png").convert_alpha()
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Professor Moore's Nightmare")
        self.player = character.Character()
        # implement an obstacles group
        self.state = "GAME"
        self.clock = pygame.time.Clock()
        self.JUMPEVENT = pygame.USEREVENT + 1

    def mainLoop(self):
        running = True
        while running:
            if self.state == "GAME":
                self.gameLoop()
            # elif self.state == "END":
            #     self.endLoop()
            # elif self.state == "START":
            #     self.startLoop()

    def gameLoop(self):
        while self.state == "GAME":
            if pygame.event.get(self.JUMPEVENT):
                self.player.jump_state = False
                pygame.time.set_timer(self.JUMPEVENT,0)
                self.player.setState("RUN")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.player.move("UP")
                    elif event.key == pygame.K_s:
                        self.player.move("DOWN")
                    elif event.key == pygame.K_SPACE:
                        self.player.jump(self.JUMPEVENT)

            self.windowSurface.blit(pygame.Surface((512, 384)),(0,0))
            self.bg.update()
            self.bg.tiles.draw(self.windowSurface)
            self.player.animObjs[self.player.state].blit(self.windowSurface, self.player.rect)
            pygame.display.flip()

            self.clock.tick(30)

    # def startLoop(self):
    #     while self.state == "START":
    #         # start screen code
    #         # draw background
    #         # display widgets
    #
    # def endLoop(self):
    #     while self.state == "END":
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT():
    #                 sys.exit()
