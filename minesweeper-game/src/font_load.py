import pygame
import os

dir = os.path.dirname(__file__)

def font_load(file):
    pygame.font.init()
    return pygame.font.Font(os.path.join(dir, "assets", file), 100)
    