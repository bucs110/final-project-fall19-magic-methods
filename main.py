#import your controller
import pygame, pyganim, character, spriteSheet, gameScreen, random


def main():
    pygame.init()

    game = Controller()
    game.mainLoop()

if __name__ == "__main__":
    main()
