from image_load import image_load
import pygame

class OpenedTile(pygame.sprite.Sprite):
    def __init__(self, x_coord=0, y_coord=0, number=0):
        super().__init__()

        self.number = number
        self.image = image_load(f"tile_{self.number}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
