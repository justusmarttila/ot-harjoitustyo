import pygame
import os

dir = os.path.dirname(__file__)

def image_load(file):
    """Funktio, jonka avulla luetaan peliin tarvittavat kuvat.

    Args:
        file (str): Kuvatiedoston nimi.

    Returns:
        pygame.image: Palauttaa pygame oliona kuvan.
    """

    image = pygame.transform.scale(pygame.image.load(os.path.join(dir, "assets", file)), (50, 50))
    return image
