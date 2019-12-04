import pygame
from src import animatedSprite


class Character(pygame.sprite.Sprite):
    def __init__(self):
        """
        Initializes Character Object
        args: self (Character Object) a reference to the object itself
        return: None
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.rect = self.image.get_rect()
        anims = [
            animatedSprite.AnimatedSprite("assets/imgs/sam_sprites.png", 0, 0,
                                          64, 64, 6, 200),
            animatedSprite.AnimatedSprite("assets/imgs/sam_sprites.png", 0, 64,
                                          64, 64, 3, 300),
            animatedSprite.AnimatedSprite("assets/imgs/sam_sprites.png", 312, 64,
                                          64, 64, 1, 200)
        ]
        anims = [
            anim.getAnimatedSprite() for anim in anims
        ]
        self.animObjs = {
            "RUN": anims[0],
            "JUMP": anims[1],
            "HURT": anims[2]
        }
        self.reset()

    def reset(self):
        """
        Resets the character variables to their initial states
        args: self (Character Object) a reference to the object itself
        return: None
        """
        self.row = 2
        self.rect.x, self.rect.y = 40, 256 + (self.row - 2) * 42
        self.lives = 3
        self.jumping = False
        self.setState("RUN")

    def setState(self, state):
        """
        Sets the new state of the character
        args: self (Character Object) a reference to the object itself
            state (string) the character's new state
        return: None
        """
        if state == "RUN":
            self.jumping = False
        self.state = state
        self.animObjs[self.state].play()

    def getHealth(self):
        """
        Gets the character's lives
        args: self (Character Object) a reference to the object itself
        return: (int) character's lives
        """
        return self.lives

    def takeDamage(self):
        """
        Reduces the character's lives by one
        args: self (Character Object) a reference to the object itself
        return: None
        """
        self.setState("HURT")
        pygame.time.set_timer(pygame.USEREVENT + 2, 400)
        self.lives -= 1

    def move(self, dir):
        """
        Moves the character up and down relative to the rows
        args: self (Character Object) a reference to the object itself
            dir (string) a direction for the character to move in
        return: None
        """
        if dir == "UP":
            if not self.row - 1 < 1:
                self.row -= 1
        elif dir == "DOWN":
            if not self.row + 1 > 3:
                self.row += 1

        self.rect.y = 256 + (self.row - 2) * 42

    def jump(self):
        """

        args: self (Character Object) a reference to the object itself
        return: None
        """
        if self.state != "JUMP":
            self.setState("JUMP")
            pygame.time.set_timer(pygame.USEREVENT + 1, 900)
