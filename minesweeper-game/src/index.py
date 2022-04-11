import pygame
from board import Board
from game_loop import GameLoop
from event_queue import EventQueue
from clock import Clock
from renderer import Renderer

lower_board_1 = [[1, -1, 2, 1, 0, 1, -1],
                 [1,  2, -1, 1, 0, 1,  1],
                 [0,  1, 1, 1, 0, 0,  0]]

top_board_1 = [[9]*7]*3

tile_size = 50

def main():

    # asetetaan laudan koko
    width = len(lower_board_1[0])
    height = len(lower_board_1)
    scaled_width = width*tile_size
    scaled_height = height*tile_size

    # ikkunan alustus
    display = pygame.display.set_mode((scaled_width, scaled_height))

    # ikkunan nimeäminen
    pygame.display.set_caption("Minesweeper")

    # alustetaan lauta, tapahtumajono, renderöijä, kello sekä peliloop
    board = Board(lower_board_1, top_board_1, tile_size)
    event_queue = EventQueue()
    renderer = Renderer(display, board)
    clock = Clock()
    game_loop = GameLoop(board, tile_size, renderer, clock, event_queue)

    # pygamen moduulien alustus
    pygame.init()
    game_loop.start()

if __name__ == "__main__":
    main()
