import pygame
from font_load import font_load
import time

class Renderer:
    def __init__(self, display, board):
        self._display = display
        self._board = board
        self._mines_left = 0
        self._font = font_load("digital-7.ttf")
        self._time = time.time()

    def render(self):
        # jäljellä olevien miinojen esittäminen vasemmassa ylänurkassa
        self._mines_left = len(self._board.mines)-len(self._board.marked)
        self._display.fill((171, 174, 171))
        pygame.draw.rect(self._display, (0, 0, 0), pygame.Rect(10, 10, 107, 82))
        self._display.blit(self._font.render(f"{self._mines_left}", True, (255, 0, 0)), (15, 10))

        # aika oikeassa ylänurkassa
        pygame.draw.rect(self._display, (0, 0, 0), pygame.Rect((len(self._board.top_map[0])*self._board.tile_size)-160, 10, 150, 82))
        if time.time()-self._time >= 999:
            self.seconds = 999
        else:
            self.seconds = time.time()-self._time
        self._display.blit(self._font.render(f"{self.seconds:.0f}", True, (255, 0, 0)), ((len(self._board.top_map[0])*self._board.tile_size)-155, 10))

        self._board.all_sprites.draw(self._display)

        pygame.display.update()
