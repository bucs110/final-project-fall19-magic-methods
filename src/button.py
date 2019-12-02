import pygame

class Button:
    def __init__(self, display, img_file, x, y):
        self.display = display
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self):
        self.display.blit(self.image, self.rect)

    def isHover(self,mouse_pos):
        if mouse_pos[0] > self.rect.x and mouse_pos[0] < self.rect.x + self.rect.width:
            if mouse_pos[1] > self.rect.y and mouse_pos[1] < self.rect.y + self.rect.height:
                return True
        return False
