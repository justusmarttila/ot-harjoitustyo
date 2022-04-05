import pygame
from image_load import image_load

class UnopenedTile(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, marked=False):
        super().__init__()

        self.marked = marked
        self._pictures = self._load_pictures()
        self.picture = self._pictures["unopened"]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.marked:
            self.picture = self._pictures["marked"]
        else:
            self.picture = self._pictures["unopened"]

    def _load_pictures(self):
        pictures = {"unopened": image_load("unopened_tile.png"), "marked": image_load("marked_tile.png")}