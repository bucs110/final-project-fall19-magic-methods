import sys
import pygame
from src import button
from src import screen
from src import gameScreen
from src import character

class Controller:
    def __init__(self):
        self.large_font = pygame.font.SysFont("Arial", 24)
        self.small_font = pygame.font.SysFont("Arial", 16)
        self.windowSurface = pygame.display.set_mode((512,384))
        icon = pygame.image.load("assets/imgs/icon.png").convert_alpha()
        pygame.display.set_icon(icon)
        pygame.display.set_caption("110 Go!")

        self.state = "START"
        self.clock = pygame.time.Clock()
        # self.JUMPEVENT = pygame.USEREVENT + 1
        self.DAMAGEEVENT = pygame.USEREVENT + 2
        self.player = character.Character()

        self.buttons = {
            "START0": button.Button(self.windowSurface, "assets/imgs/play_button.png", 270, 200),
            "START1": button.Button(self.windowSurface, "assets/imgs/play_button.png", 250, 70),
            "EXIT": button.Button(self.windowSurface, "assets/imgs/exit_temp.png", 280, 180)
        }

        self.startScreen = screen.Screen(self.windowSurface, "assets/imgs/start_screen.png")
        self.gameScreen = gameScreen.GameScreen(self.windowSurface, self.player)
        self.gameScreen.setSpeed(2)
        self.endScreen = screen.Screen(self.windowSurface, "assets/imgs/end_screen.png")

        self.SOUNDS = {
            "THEME0":pygame.mixer.Sound("assets/sounds/whiskeymusic.wav"),
            # "JUMP":pygame.mixer.Sound("assets/sounds/jump.wav"),
            "CLICK":pygame.mixer.Sound("assets/sounds/click.wav"),
            "OUCH":pygame.mixer.Sound("assets/sounds/ouch.wav")
        }
        self.SOUNDS["THEME0"].set_volume(0.2)
        self.SOUNDS["OUCH"].set_volume(0.3)

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
        while self.state == "GAME":
            # if pygame.event.get(self.JUMPEVENT):
            #     pygame.time.set_timer(self.JUMPEVENT,0)
            #     self.player.setState("RUN")
            if pygame.event.get(self.DAMAGEEVENT):
                pygame.time.set_timer(self.DAMAGEEVENT, 0)
                self.player.setState("RUN")
                self.SOUNDS["OUCH"].play()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.player.move("UP")
                    elif event.key == pygame.K_s:
                        self.player.move("DOWN")
                    # elif event.key == pygame.K_SPACE:
                    #     self.player.jump()
                    #     self.SOUNDS["JUMP"].play()

            if self.gameScreen.getScore() > 15000:
                self.gameScreen.setSpeed(10)
            elif self.gameScreen.getScore() > 10000:
                self.gameScreen.setSpeed(8)
            elif self.gameScreen.getScore() > 5000:
                self.gameScreen.setSpeed(6)

            if self.player.getHealth() == 0:
                self.state = "END"

            score_message = self.small_font.render(f"Score: {str(self.gameScreen.getScore())}", False, (255,255,255))
            self.gameScreen.update()
            self.gameScreen.getBg().draw(self.windowSurface)
            self.player.animObjs[self.player.state].blit(self.windowSurface, self.player.rect)
            for i in range(self.player.lives):
                heart = pygame.image.load("assets/imgs/heart.png").convert_alpha()
                self.windowSurface.blit(heart, (10 + (40 * i),10))
            self.windowSurface.blit(score_message, (10, 40))
            pygame.display.update()

            self.clock.tick(30)

    def startLoop(self):
        while self.state == "START":
            self.windowSurface.blit(self.startScreen.getBg(), (0,0))
            self.buttons["START0"].draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.buttons["START0"].isHover(pygame.mouse.get_pos()):
                            self.state = "GAME"
                            self.gameScreen.reset()
                            self.SOUNDS["CLICK"].play()
                            pygame.time.wait(600)
                elif event.type == pygame.QUIT:
                    sys.exit()

    def endLoop(self):
        self.SOUNDS["THEME0"].fadeout(1000)
        score_message = self.large_font.render(f"YOU SCORED {str(self.gameScreen.getScore())}", False, (255,255,255))

        while self.state == "END":
            self.windowSurface.blit(self.endScreen.getBg(), (0,0))
            self.buttons["START1"].draw()
            self.buttons["EXIT"].draw()
            self.windowSurface.blit(score_message, (50, 160))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.buttons["EXIT"].isHover(pygame.mouse.get_pos()):
                            self.state = "START"
                            self.SOUNDS["CLICK"].play()
                            pygame.time.wait(600)
                        elif self.buttons["START1"].isHover(pygame.mouse.get_pos()):
                            self.state = "GAME"
                            self.gameScreen.reset()
                            self.SOUNDS["CLICK"].play()
                            pygame.time.wait(600)
                elif event.type == pygame.QUIT:
                    sys.exit()
