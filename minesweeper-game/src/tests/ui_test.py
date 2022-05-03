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

    def test_init(self):
        self.assertEqual(self.test_ui.level, None)
