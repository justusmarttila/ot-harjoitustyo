import pygame
import unittest
from board import Board
from game_loop.game_loop import GameLoop

class StubClock:
    def tick(self, fps):
        pass
    
    def get_ticks(self):
        0

class StubEvent:
    def __init__(self, event_type, button, x, y):
        # 1 = left click, 3 = right click'
        self.button = button
        self.type = event_type
        self.pos = (x, y)

class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events

class StubRenderer:
    def render(self):
        pass

LOWER_BOARD_1 = [[1, -1, 2, 1, 0, 1, -1],
                 [1,  2, -1, 1, 0, 1,  1],
                 [0,  1, 1, 1, 0, 0,  0]]

TOP_BOARD_1 = [[9]*7]*3

TILE_SIZE = 50

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.board_1 = Board(LOWER_BOARD_1, TOP_BOARD_1, TILE_SIZE)

    def test_mine_opened(self):
        events = [StubEvent(pygame.MOUSEBUTTONUP, 1, 75, 125)]
        game_loop = GameLoop(self.board_1, TILE_SIZE, StubRenderer(), StubClock(), StubEventQueue(events))
        game_loop.start()
        self.assertTrue(self.board_1.mine_opened())

    def test_board_completed(self):
        events = [
            StubEvent(pygame.MOUSEBUTTONUP, 1, 14, 226),
            StubEvent(pygame.MOUSEBUTTONUP, 1, 223, 126),
            StubEvent(pygame.MOUSEBUTTONUP, 1, 124, 214),
            StubEvent(pygame.MOUSEBUTTONUP, 1, 125, 113),
            StubEvent(pygame.MOUSEBUTTONUP, 1, 11, 113)
        ]
        game_loop = GameLoop(self.board_1, TILE_SIZE, StubRenderer(), StubClock(), StubEventQueue(events))
        game_loop.start()
        self.assertTrue(self.board_1.is_completed())
