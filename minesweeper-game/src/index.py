from tkinter import Tk
import pygame
from board import Board
from game_loop.game_loop import GameLoop
from game_loop.event_queue import EventQueue
from game_loop.clock import Clock
from game_loop.renderer import Renderer
from board_generator import BoardGenerator
from ui.ui import UI

def main():
    """Funktio, joka vastaa käyttöliittymän sekä pelin käynnistyksestä
    """

    window = Tk()
    window.title("Minesweeper")

    main_ui = UI(window)
    main_ui.start()
    window.mainloop()

    main_board = BoardGenerator(main_ui.level[0], main_ui.level[1], main_ui.level[2])
    lower_board = main_board.generate()
    top_board = main_board.top_board
    tile_size = 50

    # asetetaan laudan koko
    scaled_width = len(lower_board[0])*tile_size
    scaled_height = len(lower_board)*tile_size

    # ikkunan alustus
    display = pygame.display.set_mode((scaled_width, scaled_height+100))

    # ikkunan nimeäminen
    pygame.display.set_caption("Minesweeper")

    # alustetaan lauta, tapahtumajono, renderöijä, kello sekä peliloop
    main_board = Board(lower_board, top_board, tile_size)
    event_queue = EventQueue()
    renderer = Renderer(display, main_board)
    clock = Clock()
    game_loop = GameLoop(main_board, tile_size, renderer, clock, event_queue)

    # pygamen moduulien alustus
    pygame.init()
    game_loop.start()

if __name__ == "__main__":
    main()
