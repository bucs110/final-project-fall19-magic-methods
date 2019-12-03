#import your controller
from src import controller
import pygame

def main():
    pygame.mixer.pre_init(frequency=48000)
    pygame.init()

    game = controller.Controller()
    game.mainLoop()

if __name__ == "__main__":
    main()
