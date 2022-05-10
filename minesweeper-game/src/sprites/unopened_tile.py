from image_load import image_load
import pygame

class UnopenedTile(pygame.sprite.Sprite):
    """Luokka, joka kuvaa avaamatonta laattaa.

    Args:
        pygame (pygame.sprite): Luokka perii pygame-kirjaston sprite-olioiden ominaisuudet.
    """

    def __init__(self, x_coord=0, y_coord=0, marked=False, opened=False):
        """Konstruktori, joka luo yksittäisen uuden avaamattoman laatan.

        Args:
            x_coord (int): Laatan x-koordinaatti. Defaults to 0.
            y_coord (int): Laatan y-koordinaatti. Defaults to 0.
            marked (bool): Tieto onko laatta merkattu. Defaults to False.
            opened (bool): Tieto onko laatta avattu. Defaults to False.
        """

        super().__init__()

        self.marked = marked
        self.opened = opened
        self._pictures = self._load_pictures()
        self.image = self._pictures["unopened"]
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord

    def update(self):
        """Funktio, jonka avulla vaihdetaan piirrettävää kuvaa riippuen laatan tilasta
        """

        # valitse merkattu kuva
        if self.marked:
            self.image = self._pictures["marked"]
        # valitse läpinäkyvä kuva
        elif self.opened:
            self.image = self._pictures["opened"]
        # valitse avaamaton kuva
        else:
            self.image = self._pictures["unopened"]

    def _load_pictures(self):
        """Funktio, jonka avulla alustetaan sanakirja tarvittavista kuvista

        Returns:
            dict: sanakirja, joka sisältää kuvat avaamattomasta,
            merkatusta sekä läpinäkyvästä laatasta
        """

        pictures = {"unopened": image_load("unopened_tile.png"),
                    "marked": image_load("marked_tile.png"),
                    "opened": image_load("blank.png")}
        return pictures
