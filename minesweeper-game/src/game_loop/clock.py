import pygame

class Clock:
    """Luokka, jonka avulla määrätään game_loopille tahti.
    
    Attributes:
        clock: Pygamekirjaston kello.
    """

    def __init__(self):
        """Luokan konstruktori luo uuden kellon.

        Args:
            clock: Pygamekirjaston kello.
        """

        self._clock = pygame.time.Clock()

    def tick(self, fps):
        """Asettaa tietyn tahdin kellolle.

        Args:
            fps (Integer): kuinka monta kuvaa piirretään sekunnissa.
        """

        self._clock.tick(fps)

    def get_ticks(self):
        """Palauttaa millisekuntien määrän siitä hetkestä kun kutsuttiin pygame.init()

        Returns:
            float: millisekunnit pygame.init() kutsusta
        """
        return pygame.time.get_ticks()