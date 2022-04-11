import pygame
from sprites.opened_tile import OpenedTile
from sprites.unopened_tile import UnopenedTile
from sprites.mine import Mine


class Board:
    def __init__(self, lower_map, top_map, tile_size):
        self.top_map = top_map
        self.lower_map = lower_map
        self.tile_size = tile_size

        # alemman matriisin spritet
        self.zeroes = pygame.sprite.Group()
        self.ones = pygame.sprite.Group()
        self.twos = pygame.sprite.Group()
        self.threes = pygame.sprite.Group()
        self.fours = pygame.sprite.Group()
        self.fives = pygame.sprite.Group()
        self.sixes = pygame.sprite.Group()
        self.sevens = pygame.sprite.Group()
        self.eights = pygame.sprite.Group()
        self.mines = pygame.sprite.Group()

        # ylemmän matriisin spritet
        self.unopened = pygame.sprite.Group()
        self.marked = pygame.sprite.Group()
        self.opened = pygame.sprite.Group()

        self.all_number_sprites = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_lower_layer_sprites(lower_map)
        self._initialize_top_layer_sprites(top_map)
        self._add_all_sprites()
        self._add_all_numbers()

    # laatan avaaminen
    def open_tile(self, x, y):
        for tile in self.unopened:
            if tile.rect.collidepoint(x, y):
                tile.opened = True
                tile.update()
                self.unopened.remove(tile)
                self.opened.add(tile)

    # miinan merkkaus
    def mark_tile(self, x, y):
        if self.unmark_tile(x, y):
            return

        # merkkaamattoman merkkaus
        for tile in self.unopened:
            if tile.rect.collidepoint(x, y):
                tile.marked = True
                tile.update()
                self.unopened.remove(tile)
                self.marked.add(tile)
        
    # jos miina on jo merkattu voidaan myös merkkaus poistaa
    def unmark_tile(self, x, y):
        for tile in self.marked:
            if tile.rect.collidepoint(x, y):
                tile.marked = False
                tile.update()
                self.marked.remove(tile)
                self.unopened.add(tile)
                return True

    # tarkista onko miina avattu
    def mine_opened(self):
        for tile in self.opened:
            if len(self._get_colliding_targets(tile, self.mines)) > 0:
                return True
        return False

    # tarkista onko taso läpäisty
    def is_completed(self):
        if self._all_mines_marked() and self._all_number_tiles_opened():
            return True
        return False

    # tarkista onko jokainen miina merkattu
    def _all_mines_marked(self):
        for tile in self.marked:
            if len(self._get_colliding_targets(tile, self.mines)) == 0:
                return False
        return True

    # tarkista onko jokainen numero avattu
    def _all_number_tiles_opened(self):
        for tile in self.all_number_sprites:
            if len(self._get_colliding_targets(tile, self.opened)) == 0:
                return False
        return True

    def _get_colliding_targets(self, sprite, sprite_group):
        return pygame.sprite.spritecollide(sprite, sprite_group, False)

    # alustetaan alemman matriisin spritet
    def _initialize_lower_layer_sprites(self, lower_map):
        width = len(lower_map[0])
        height = len(lower_map)

        for y in range(height):
            for x in range(width):
                tile = lower_map[y][x]
                scale_x = x*self.tile_size
                scale_y = y*self.tile_size

                if tile == 0:
                    self.zeroes.add(OpenedTile(scale_x, scale_y, 0))
                elif tile == 1:
                    self.ones.add(OpenedTile(scale_x, scale_y, 1))
                elif tile == 2:
                    self.twos.add(OpenedTile(scale_x, scale_y, 2))
                elif tile == 3:
                    self.threes.add(OpenedTile(scale_x, scale_y, 3))
                elif tile == 4:
                    self.fours.add(OpenedTile(scale_x, scale_y, 4))
                elif tile == 5:
                    self.fives.add(OpenedTile(scale_x, scale_y, 5))
                elif tile == 6:
                    self.sixes.add(OpenedTile(scale_x, scale_y, 6))
                elif tile == 7:
                    self.sevens.add(OpenedTile(scale_x, scale_y, 7))
                elif tile == 8:
                    self.eights.add(OpenedTile(scale_x, scale_y, 8))
                elif tile == -1:
                    self.mines.add(Mine(scale_x, scale_y))

    # alustetaan ylemmän matriisin spritet
    def _initialize_top_layer_sprites(self, top_map):
        width = len(top_map[0])
        height = len(top_map)

        for y in range(height):
            for x in range(width):
                tile = top_map[y][x]
                scale_x = x*self.tile_size
                scale_y = y*self.tile_size
                self.unopened.add(UnopenedTile(scale_x, scale_y))


    # lisätään kaikki spritet listaan, jotta piirtäminen näytölle helpompaa
    def _add_all_sprites(self):
        self.all_sprites.add(self.zeroes, self.ones, self.twos, self.threes,
                            self.fours, self.fives, self.sixes, self.sevens, 
                            self.eights, self.mines,self.unopened, self.marked)
    
    def _add_all_numbers(self):
        self.all_number_sprites.add(self.zeroes, self.ones, self.twos, 
                                    self.threes, self.fours, self.fives, 
                                    self.sixes, self.sevens, self.eights)
