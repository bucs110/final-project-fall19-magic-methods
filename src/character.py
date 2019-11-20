import pygame
import animatedSprite

# for an animated sprite
# (img_file, x, y,
# width, height, n_frames, frame_length)
class Character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64,64))
        self.rect = self.image.get_rect()
        self.row = 2
        self.rect.x, self.rect.y = 40, 256 + (self.row - 2) * 42
        self.lives = 3
        self.jumping = False
        anims = [
            animatedSprite.AnimatedSprite("assets/temp_sprite.png",0,64,
                            64,64,6,200),
            animatedSprite.AnimatedSprite("assets/temp_sprite.png",0,128,
                            64,64,3,300)
        ]
        anims = [
            anim.getAnimatedSprite() for anim in anims
        ]
        self.animObjs = {
            "RUN":anims[0],
            "JUMP":anims[1]
        }
        self.setState("RUN")

    def setState(self,state):
        self.state = state
        self.animObjs[self.state].play()

    def takeDamage(self):
        self.lives -= 1
        return self.lives < 1


    def move(self,dir):
        if dir == "UP":
            if not self.row - 1 < 1:
                self.row -= 1
        elif dir == "DOWN":
            if not self.row + 1 > 3:
                self.row += 1

        self.rect.y = 256 + (self.row - 2) * 42

    def jump(self, event):
        if self.state != "JUMP":
            self.setState("JUMP")
            pygame.time.set_timer(event, 900)
            print("started jump")
