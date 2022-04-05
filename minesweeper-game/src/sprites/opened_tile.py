import pygame
from image_load import image_load

class OpenedTile(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, number=0, opened=False):
        super().__init__()

        self.opened = opened
        self.number = number

        self._pictures = self._load_pictures()

        self.picture = self._pictures["unopened"]
        self.rect = self.picture.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.opened:
            self.picture = self._pictures["opened"]
        else:
            self.picture = self._pictures["unopened"]
    
    def _load_pictures(self):
        pictures = {"unopened": image_load("unopened_tile.png"), "opened": image_load(f"tile_{self.number}")}
        return pictures