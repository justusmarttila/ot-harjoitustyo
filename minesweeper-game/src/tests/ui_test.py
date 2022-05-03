import unittest
from tkinter import Tk
from ui.ui import UI

class TestUI(unittest.TestCase):
    def setUp(self):
        self.window = Tk()
        self.window.title("test")
        self.test_ui = UI(self.window)
        self.test_ui.start()
        self.window.mainloop()

    def test_beginner_button(self):
        self.assertEqual(self.test_ui.level, (9, 9, 10))
