import pygame
import animatedSprite

# for an animated sprite
# (self, img_file, x, y,
# width, height, n_frames, frame_length)
class Character(pygame.sprite.Sprite):
    def __init__(self):
        self.row = 2
        self.lives = 3
        self.jumping = False
        anims = [
            aniamtedSprite.AnimatedSprite("assets/temp_sprite.png",0,64,
                            64,64,6,200),
                            
        ]
