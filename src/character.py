import pygame
from src import animatedSprite

class Character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64,64))
        self.rect = self.image.get_rect()
        anims = [
            animatedSprite.AnimatedSprite("assets/imgs/sam_sprites.png",0,0,
                            64,64,6,200),
            animatedSprite.AnimatedSprite("assets/imgs/sam_sprites.png",0,64,
                            64,64,3,300),
            animatedSprite.AnimatedSprite("assets/imgs/sam_sprites.png",312,64,
                            64,64,1,200)
        ]
        anims = [
            anim.getAnimatedSprite() for anim in anims
        ]
        self.animObjs = {
            "RUN":anims[0],
            "JUMP":anims[1],
            "HURT":anims[2]
        }
        self.reset()

    def reset(self):
        self.row = 2
        self.rect.x, self.rect.y = 40, 256 + (self.row - 2) * 42
        self.lives = 3
        self.jumping = False
        self.setState("RUN")

    def setState(self,state):
        if state == "RUN":
            self.jumping = False
        self.state = state
        self.animObjs[self.state].play()

    def getHealth(self):
        return self.lives

    def takeDamage(self):
        self.setState("HURT")
        pygame.time.set_timer(pygame.USEREVENT + 2,400)
        self.lives -= 1

    def move(self,dir):
        if dir == "UP":
            if not self.row - 1 < 1:
                self.row -= 1
        elif dir == "DOWN":
            if not self.row + 1 > 3:
                self.row += 1

        self.rect.y = 256 + (self.row - 2) * 42

    def jump(self):
        if self.state != "JUMP":
            self.setState("JUMP")
            pygame.time.set_timer(pygame.USEREVENT + 1, 900)
