class Controller:
    def __init__(self):
        self.windowSurface = pygame.display.set_mode((512,384))
        pygame.display.set_caption("Professor Moore's Nightmare")
        self.player = character.Character()
        # implement an obstacles group
        self.state = "GAME"

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
            if pygame.event.get(endJump):
                player.jump_state = False
                pygame.time.set_timer(25,0)
                player.state = "RUN"
                player.anim_state[player.state].play()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT():
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            player.changePosition(-42)
                        elif event.key == pygame.K_s:
                            player.changePosition(42)
                        elif event.key == pygame.K_SPACE:
                            player.jump()

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
