import pygame
from sprites.opened_tile import OpenedTile
from sprites.unopened_tile import UnopenedTile
from sprites.mine import Mine

class Board:
    def __init__(self, map, tile_size):
        self.tile_size = tile_size
        self.opened_tiles = pygame.sprite.Group()
        self.unopened_tiles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

    def _init_sprites(self, map):
        width = len(map[0])
        height = len(map)

        for y in range(height):
            for x in range(width):
                tile = map[y][x]
                scale_x  = x*self.tile_size
                scale_y = y*self.tile_size

                

                