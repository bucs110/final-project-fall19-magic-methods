import pygame


class Button:
    def __init__(self, display, img_file, x, y):
        """
        Initializes Button Object
        args: self (Button Object) a reference to the object itself
            display (Surface) a surface that Button draws on
            img_file (string) a path to an image
            x (int) top coordinate of a surface
            y (int) left coordinate of a surface
        return: None
        """
        self.display = display
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self):
        """
        Draws images to the screen
        args: self (Button Object) a reference to the object itself
        return: None
        """
        self.display.blit(self.image, self.rect)

    def isHover(self, mouse_pos):
        """
        Checks if the cursor is over a button
        args: self (Button Object) a reference to the object itself
            mouse_pos (tuple) checks the position of the cursor
        return: (Boolean) True or False
        """
        if mouse_pos[0] > self.rect.x and mouse_pos[0] < self.rect.x + self.rect.width:
            if mouse_pos[1] > self.rect.y and mouse_pos[1] < self.rect.y + self.rect.height:
                return True
        return False
