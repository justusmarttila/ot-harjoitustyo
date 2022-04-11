from board import Board
import unittest

LOWER_BOARD_1 = [[1, -1, 2, 1, 0, 1, -1],
                 [1,  2, -1, 1, 0, 1,  1],
                 [0,  1, 1, 1, 0, 0,  0]]

TOP_BOARD_1 = [[9]*7]*3

TILE_SIZE = 50

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board_1 = Board(LOWER_BOARD_1, TOP_BOARD_1, TILE_SIZE)

    def test_initialized_correctly(self):
        self.assertEqual(self.board_1.tile_size, 50)
        self.assertEqual(len(self.board_1.all_sprites), 42)
        self.assertEqual(len(self.board_1.ones), 10)
        self.assertEqual(len(self.board_1.twos), 2)
        self.assertEqual(len(self.board_1.zeroes), 6)
        self.assertEqual(len(self.board_1.unopened), 21)
        self.assertEqual(len(self.board_1.opened), 0)

    def test_can_open_tile(self):
        original_unopened_count = len(self.board_1.unopened)
        original_opened_count = len(self.board_1.opened)
        self.board_1.open_tile(25, 25)
        self.assertEqual(original_unopened_count, len(self.board_1.unopened)+1)
        self.assertEqual(original_opened_count, len(self.board_1.opened)-1)

    def test_can_mark_tile(self):
        original_unopened_count = len(self.board_1.unopened)
        original_marked_count = len(self.board_1.marked)
        self.board_1.mark_tile(25, 25)
        self.assertEqual(original_unopened_count, len(self.board_1.unopened)+1)
        self.assertEqual(original_marked_count, len(self.board_1.marked)-1)

    def test_if_marked_unmark(self):
        original_unopened_count = len(self.board_1.unopened)
        original_marked_count = len(self.board_1.marked)
        self.board_1.mark_tile(25, 25)
        self.board_1.mark_tile(25, 25)
        self.assertEqual(original_unopened_count, len(self.board_1.unopened))
        self.assertEqual(original_marked_count, len(self.board_1.marked))

    def test_mine_opened(self):
        self.board_1.open_tile(75, 25)
        self.assertTrue(self.board_1.mine_opened())
        
