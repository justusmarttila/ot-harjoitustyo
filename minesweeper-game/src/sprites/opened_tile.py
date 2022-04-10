from image_load import image_load
import pygame
import os
import sys
dir = os.path.dirname("image_load.py")
sys.path.append(dir)


class OpenedTile(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, number=0):
        super().__init__()

        self.number = number
        self.image = image_load(f"tile_{self.number}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
