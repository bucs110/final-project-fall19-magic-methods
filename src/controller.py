import sys
import pygame
import character

class Controller:
    def __init__(self):
        self.windowSurface = pygame.display.set_mode((512,384))
        self.bg = pygame.Surface((512,384))
        self.bg.fill((255,255,255))
        icon = pygame.image.load("assets/SAM.png").convert_alpha()
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Professor Moore's Nightmare")
        self.player = character.Character()
        # implement an obstacles group
        self.state = "GAME"
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
                print("ended jump")

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

            self.windowSurface.blit(self.bg,(0,0))
            self.player.animObjs[self.player.state].blit(self.windowSurface, self.player.rect)
            pygame.display.flip()

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
