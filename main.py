#import your controller
import controller
import pygame

def main():
    pygame.init()

    game = controller.Controller()
    game.mainLoop()

if __name__ == "__main__":
    main()
