import pygame
from image_load import image_load

class UnopenedTile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = image_load("unopened_tile.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
