import pygame
from board import Board
from game_loop.game_loop import GameLoop
from game_loop.event_queue import EventQueue
from game_loop.clock import Clock
from game_loop.renderer import Renderer
from board_generator import BoardGenerator

from tkinter import Tk
from ui.ui import UI

def main():

    window = Tk()
    window.title("Minesweeper")

    ui = UI(window)
    ui.start()
    
    window.mainloop()

    BOARD = BoardGenerator(ui.level[0], ui.level[1], ui.level[2])
    LOWER_BOARD_1 = BOARD.generate()
    TOP_BOARD_1 = BOARD.top_board
    TILE_SIZE = 50

    # asetetaan laudan koko
    width = len(LOWER_BOARD_1[0])
    height = len(LOWER_BOARD_1)
    scaled_width = width*TILE_SIZE
    scaled_height = height*TILE_SIZE

    # ikkunan alustus
    display = pygame.display.set_mode((scaled_width, scaled_height+100))

    # ikkunan nimeäminen
    pygame.display.set_caption("Minesweeper")

    # alustetaan lauta, tapahtumajono, renderöijä, kello sekä peliloop
    board = Board(LOWER_BOARD_1, TOP_BOARD_1, TILE_SIZE)
    event_queue = EventQueue()
    renderer = Renderer(display, board)
    clock = Clock()
    game_loop = GameLoop(board, TILE_SIZE, renderer, clock, event_queue)

    # pygamen moduulien alustus
    pygame.init()
    game_loop.start()

if __name__ == "__main__":
    main()
