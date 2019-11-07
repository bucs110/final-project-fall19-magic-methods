import pygame
import animatedSprite

# for an animated sprite
# (img_file, x, y,
# width, height, n_frames, frame_length)
class Character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.__init__()
        self.row = 2
        self.lives = 3
        self.jumping = False
        anims = [
            animatedSprite.AnimatedSprite("assets/temp_sprite.png",0,64,
                            64,64,6,200),
            animatedSprite.AnimatedSprite("assets/temp_sprite.png",0,128,
                            64,64,3,200)
        ]
        anims = [
            anim.getAnimatedSprite() for anim in anims
        ]
        self.animObjs = {
            "RUN":anims[0],
            "JUMP":anims[1]
        }
        self.state = "RUN"

    def setState(self,state):
        self.state = state

    def move(self,dir):
        if dir == "UP":
            if not self.row - 1 < 1:
                self.row -= 1
        elif dir == "DOWN":
            if not self.row + 1 > 3:
                self.row += 1

    def jump(self):
        if self.state != "JUMP":
            self.state = "JUMP"
