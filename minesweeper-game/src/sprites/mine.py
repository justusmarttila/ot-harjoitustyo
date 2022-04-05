import pygame
from image_load import image_load

class Mine(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, marked=False):
        super().__init__()

        self.picture = image_load("mine.png")
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y