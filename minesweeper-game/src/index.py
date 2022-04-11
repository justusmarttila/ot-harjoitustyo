import pygame
from board import Board
from game_loop import GameLoop
from event_queue import EventQueue
from clock import Clock
from renderer import Renderer

LOWER_BOARD_1 = [[1, -1, 2, 1, 0, 1, -1],
                 [1,  2, -1, 1, 0, 1,  1],
                 [0,  1, 1, 1, 0, 0,  0]]

TOP_BOARD_1 = [[9]*7]*3

TILE_SIZE = 50

def main():

    # asetetaan laudan koko
    width = len(LOWER_BOARD_1[0])
    height = len(LOWER_BOARD_1)
    scaled_width = width*TILE_SIZE
    scaled_height = height*TILE_SIZE

    # ikkunan alustus
    display = pygame.display.set_mode((scaled_width, scaled_height))

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
