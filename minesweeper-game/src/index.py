import pygame
from board import Board

lower_board_1 = [[1, -1, 2, 1, 0, 1, -1],
                 [1,  2,-1, 1, 0, 1,  1],
                 [0,  1, 1, 1, 0, 0,  0]]

top_board_1 = [[9]*7]*3

tile_size = 50

def main():
    width = len(lower_board_1[0])
    height = len(lower_board_1)
    scaled_width = width*tile_size
    scaled_height = height*tile_size

    display = pygame.display.set_mode((scaled_width, scaled_height))

    pygame.display.set_caption("Minesweeper")

    board = Board(lower_board_1, top_board_1, tile_size)

    pygame.init()

    if __name__ == "__main__":
        main()