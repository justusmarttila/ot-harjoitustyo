from image_load import image_load
import pygame

class OpenedTile(pygame.sprite.Sprite):
    """Avattua laattaa kuvaava sprite-luokka.

    Args:
        pygame (pygame.sprite): Luokka perii pygame-kirjaston sprite-olioiden ominaisuudet.
    """

    def __init__(self, x_coord=0, y_coord=0, number=0):
        """Konstruktori, joka luo yksittäisen OpenedTile-olion.

        Args:
            x_coord (int): Laatan x-koordinaatti laudalla. Defaults to 0.
            y_coord (int): Laatan y-koordinaatti laudalla. Defaults to 0.
            number (int): Numero kertoo montako miinaa sen ympärillä olevissa 8 ruudussa on.
            (-1 tarkoittaa miinaa). Defaults to 0.
        """

        super().__init__()

        self.number = number
        self.image = image_load(f"tile_{self.number}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
