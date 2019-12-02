import sys
import pygame
from src import button
from src import startScreen
from src import gameScreen
from src import endScreen
from src import character

class Controller:
    def __init__(self):
        self.windowSurface = pygame.display.set_mode((512,384))
        self.clock = pygame.time.Clock()
        self.player = character.Character()
        self.state = "START"
        self.JUMPEVENT = pygame.USEREVENT + 1
        self.DAMAGEEVENT = pygame.USEREVENT + 2

        icon = pygame.image.load("assets/SAM.png").convert_alpha()
        pygame.display.set_icon(icon)
        pygame.display.set_caption("110 Go!")
        self.buttons = {
            "start": button.Button(self.windowSurface, "assets/play_button.png", 270, 200)
        }

        self.startScreen = startScreen.StartScreen(self.windowSurface, "assets/start_temp.png")
        self.gameScreen = gameScreen.GameScreen(self.windowSurface, self.player)
        self.gameScreen.setSpeed(2)
        self.endScreen = endScreen.EndScreen(self.windowSurface, "assets/end_temp.jpg")

        self.SOUNDS = {
            "THEME0":pygame.mixer.Sound("assets/sounds/LoopFrogger.wav"),
            "JUMP":pygame.mixer.Sound("assets/sounds/jump.wav"),
            "CLICK":pygame.mixer.Sound("assets/sounds/click.wav"),
            "RUN":pygame.mixer.Sound("assets/sounds/run.wav"),
        }
        self.SOUNDS["THEME0"].set_volume(0.2)

    def mainLoop(self):
        running = True
        while running:
            if self.state == "START":
                self.startLoop()
            elif self.state == "GAME":
                self.gameLoop()
            elif self.state == "END":
                self.endLoop()

    def gameLoop(self):
        self.SOUNDS["THEME0"].play(-1)
        self.SOUNDS["RUN"].play(-1)
        while self.state == "GAME":
            if pygame.event.get(self.JUMPEVENT):
                pygame.time.set_timer(self.JUMPEVENT,0)
                self.player.setState("RUN")
            elif pygame.event.get(self.DAMAGEEVENT):
                pygame.time.set_timer(self.DAMAGEEVENT,0)
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
                        self.player.jump()
                        self.SOUNDS["JUMP"].play()

            if self.gameScreen.getScore() > 15000:
                self.gameScreen.setSpeed(8)
            elif self.gameScreen.getScore() > 10000:
                self.gameScreen.setSpeed(6)
            elif self.gameScreen.getScore() > 5000:
                self.gameScreen.setSpeed(4)

            if self.player.getHealth() == 0:
                self.state = "END"

            self.gameScreen.update()
            self.gameScreen.getBg().draw(self.windowSurface)
            self.player.animObjs[self.player.state].blit(self.windowSurface, self.player.rect)
            pygame.display.update()

            self.clock.tick(30)

    def startLoop(self):
        while self.state == "START":
            self.windowSurface.blit(self.startScreen.getBg(), (0,0))
            self.buttons["start"].draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.buttons["start"].isHover(pygame.mouse.get_pos()):
                            self.state = "GAME"
                            self.SOUNDS["CLICK"].play()
                            pygame.time.wait(600)
                elif event.type == pygame.QUIT:
                    sys.exit()

    def endLoop(self):
        while self.state == "END":
            self.windowSurface.blit(self.endScreen.getBg(), (0,0))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
