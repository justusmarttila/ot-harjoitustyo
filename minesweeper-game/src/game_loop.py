import pygame

class GameLoop:
    def __init__(self, board, tile_size, renderer, clock, event_queue):
        self._board = board
        self._clock = clock
        self._tile_size = tile_size
        self._renderer = renderer
        self._event_queue = event_queue

    def start(self):
        while True:
            if self._traverse_events() == False:
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
        
        # käy läpi tapahtumat
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
        self._renderer.render()
