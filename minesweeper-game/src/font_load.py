import pygame
import os

dir = os.path.dirname(__file__)

def font_load(file):
    """Funktio, jonka avulla ladataan fontti projektiin.

    Args:
        file (str): Fontin tiedoston nimi.

    Returns:
        pygame.font.Font: Palauttaa 100 kokoisen fontin jatkokäyttöä varten.
    """

    pygame.font.init()
    return pygame.font.Font(os.path.join(dir, "assets", file), 100)
    