import pygame
from sprites.opened_tile import OpenedTile
from sprites.unopened_tile import UnopenedTile

class Board:
    def __init__(self, map: list, square_size):
        self.square_size = square_size