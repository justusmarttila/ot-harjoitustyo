from board import Board
import unittest
import os
import sys
dir = os.path.dirname("board.py")
sys.path.append(dir)

lower_board_1 = [[1, -1, 2, 1, 0, 1, -1],
                 [1,  2, -1, 1, 0, 1,  1],
                 [0,  1, 1, 1, 0, 0,  0]]

top_board_1 = [[9]*7]*3

tile_size = 50


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board_1 = Board(lower_board_1, top_board_1, tile_size)

    def test_initialized_correctly(self):
        self.assertEqual(self.board_1.tile_size, 50)
        self.assertEqual(len(self.board_1.all_sprites), 42)
        self.assertEqual(len(self.board_1.ones), 10)
        self.assertEqual(len(self.board_1.twos), 2)
        self.assertEqual(len(self.board_1.zeroes), 6)
        self.assertEqual(len(self.board_1.unopened), 21)
