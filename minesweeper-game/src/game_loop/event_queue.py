import pygame

class EventQueue:
    """Luokka, jonka avulla voidaan käsitellä pygame tapahtumien ketjua
    """
    def get(self):
        return pygame.event.get()
