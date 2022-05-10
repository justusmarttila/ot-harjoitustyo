import pygame

class EventQueue:
    """Luokka, jonka avulla voidaan käsitellä pygame tapahtumien ketjua
    """
    def get(self):
        """Funktio, joka palauttaa pygame tapahtumien listan

        Returns:
            list: Palauttaa pygame tapahtumat listana
        """
        return pygame.event.get()
