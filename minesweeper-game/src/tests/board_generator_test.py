import unittest
from board_generator import BoardGenerator

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board_1 = BoardGenerator(30, 16, 99)

    def test_init(self):
        self.assertEqual(self.board_1.width, 30)
        self.assertEqual(self.board_1.height, 16)
        self.assertEqual(self.board_1.mines, 99)
        self.assertEqual(len(self.board_1.top_board[0]), 30)
        self.assertEqual(len(self.board_1.top_board), 16)

    def test_generate(self):
        board = self.board_1.generate()
        self.assertEqual(len(board[0]), 30)
        self.assertEqual(len(board), 16)
