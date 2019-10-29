#import your controller
import pygame, pyganim,character,spriteSheet,game

pygame.init()

def main():
    player = character.Character()
    gameScreen = game.Game(player,"assets/temp_sprite.png")
    endJump = pygame.USEREVENT + 1
    running = True

    while running:
        #Create an instance on your controller object
        if pygame.event.get(endJump):
            player.jump_state = False
            pygame.time.set_timer(25,0)
            player.y += 20

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.y -= 64
                elif event.key == pygame.K_s:
                    player.y += 64
                elif event.key == pygame.K_SPACE:
                    player.jump()

        gameScreen.update()
        gameScreen.render()
    pygame.quit()

if __name__ == "__main__":
    main()
