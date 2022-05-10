import pygame

class GameLoop:
    """Luokka, joka toimii pelin pääsilmukkana eli käsittelee tapahtumat.

    Attributes:
        board: Board-olio, joka kuvaa pelilautaa eli kuinka monta miinaa laudalla on
        ja niiden sijaintia sekä avattuja, avaamattomia sekä merkattuja laattoja.
        clock: Clock-olio, joka toimii fps:n asettamisen työkaluna.
        tile_size: Integer-arvo, jonka avulla määritellään minkä kokoinen pelilauta piirretään.
        renderer: Renderer-olio, joka vastaa kaikesta pelissä tapahtuvasta renderöimisestä
        eli asioiden piirtämisestä peli-ikkunaan.
        event_queue: EventQueue-olio, joka helpottaa pelitapahtumien läpikäymistä.
    """

    def __init__(self, board, tile_size, renderer, clock, event_queue):
        """Konstruktori, joka luo uuden pelisilmukan.

        Args:
            board: Board-olio, joka kuvaa pelilautaa eli kuinka monta miinaa laudalla on
            ja niiden sijaintia sekä avattuja, avaamattomia sekä merkattuja laattoja.
            clock: Clock-olio, joka toimii fps:n asettamisen työkaluna.
            tile_size: Integer-arvo, jonka avulla määritellään minkä kokoinen pelilauta piirretään.
            renderer: Renderer-olio, joka vastaa kaikesta pelissä tapahtuvasta renderöimisestä
            eli asioiden piirtämisestä peli-ikkunaan.
            event_queue: EventQueue-olio, joka helpottaa pelitapahtumien läpikäymistä.
        """

        self._board = board
        self._clock = clock
        self._tile_size = tile_size
        self._renderer = renderer
        self._event_queue = event_queue

    def start(self):
        """Aloittaa pelin pääsilmukan, tarkistaa onko painettu ruksia,

        piirtää näytön, sulkee pelin, jos avataan miina tai kaikki miinat on löydetty.
        """

        while True:
            if self._traverse_events() is False:
                break

            # kutsutaan renderer
            self._render()

            # onko miina avattu
            if self._board.mine_opened():
                break

            # onko peli läpäisty
            if self._board.is_completed():
                break

            # asetetaan fps 60
            self._clock.tick(60)

    def _traverse_events(self):
        """Pelitapahtumien läpikäyminen, kuten hiiren 1 painikkeella laatan avaaminen
        sekä hiiren 2 painikkeella laatan merkkaaminen.

        Returns:
            Boolean: Suljettaessa peli ruksista palautetaan pääsilmukalle False ja ikkuna suljetaan.
        """

        for event in self._event_queue.get():
            if event.type == pygame.MOUSEBUTTONUP:

                # klikkauksen koordinaatit
                mouse_x, mouse_y = event.pos[0], event.pos[1]

                # laatan avaaminen
                if event.button == 1:
                    self._board.open_tile(mouse_x, mouse_y)

                # laatan merkkaaminen
                elif event.button == 3:
                    self._board.mark_tile(mouse_x, mouse_y)

            # ikkunan sulkeminen
            elif event.type == pygame.QUIT:
                return False

    def _render(self):
        """kutsutaan Renderer olion render metodia ja piirretään näyttö.
        """
        self._renderer.render()
