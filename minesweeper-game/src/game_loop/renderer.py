import pygame
from font_load import font_load

class Renderer:
    def __init__(self, display, board):
        self._display = display
        self._board = board
        self._mines_left = 0
        self._font = font_load("digital-7.ttf")

    def render(self):
        self._mines_left = len(self._board.mines)-len(self._board.marked)
        self._display.fill((171, 174, 171))
        pygame.draw.rect(self._display, (100, 100, 100), pygame.Rect(10, 10, 107, 82))
        self._display.blit(self._font.render(f"{self._mines_left}", True, (255, 0, 0)), (15, 10))
        self._board.all_sprites.draw(self._display)

        pygame.display.update()
