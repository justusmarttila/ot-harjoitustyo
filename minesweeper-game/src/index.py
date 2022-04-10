import pygame
from board import Board

lower_board_1 = [[1, -1, 2, 1, 0, 1, -1],
                 [1,  2, -1, 1, 0, 1,  1],
                 [0,  1, 1, 1, 0, 0,  0]]

top_board_1 = [[9]*7]*3

tile_size = 50


def main():
    #asetetaan laudan koko
    width = len(lower_board_1[0])
    height = len(lower_board_1)
    scaled_width = width*tile_size
    scaled_height = height*tile_size

    #ikkunan alustus
    display = pygame.display.set_mode((scaled_width, scaled_height))

    #ikkunan nimeäminen
    pygame.display.set_caption("Minesweeper")

    #alustetaan lauta
    board = Board(lower_board_1, top_board_1, tile_size)

    #pygamen moduulien alustus
    pygame.init()

    #all_sprites piirtäminen ikkunaan
    board.all_sprites.draw(display)

    running = True

    #pelisilmukka
    while running:
        for event in pygame.event.get():

            #peli ikkunan sulkeminen
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
