import pygame
import os

dir = os.path.dirname(__file__)

def image_load(file):
    image = pygame.image.load(os.path.join(dir, "assets", file))
    return image
