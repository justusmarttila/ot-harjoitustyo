import pygame
from image_load import image_load

class OpenedTile(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, number=0):
        super().__init__()

        self.number = number
        self.picture = image_load(f"tile_.{self.number}.png")
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y

    