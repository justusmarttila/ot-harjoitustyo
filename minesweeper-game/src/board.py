import pygame
from sprites.opened_tile import OpenedTile
from sprites.unopened_tile import UnopenedTile

class Board:
    """Luokka, joka vastaa pelilautaan liittyvistä toiminnoista
    """

    def __init__(self, lower_map, top_map, tile_size):
        """Konstruktori, joka luo yksittäisen uuden pelilaudan.

        Args:
            lower_map (list): Alempi eli numeroita ja miinoja kuvaava lauta.
            top_map (list): Ylempi eli avaamattomia laattoja kuvaava lauta.
            tile_size (int): Yksittäisen laatan koko.
        """

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
        self.numbers_no_zeroes = pygame.sprite.Group()

        self._initialize_lower_layer_sprites(lower_map)
        self._initialize_top_layer_sprites(top_map)
        self._add_all_sprites()
        self._add_all_numbers()
        self._add_numbers_no_zeroes()

    def open_tile(self, mouse_x, mouse_y):
        """Laatan avaamisesta huolehtiva funktio.

        Args:
            mouse_x (float): Hiiren vasemman painikkeen painamisen x-koordinaatti.
            mouse_y (float): Hiiren vasemman painikkeen painamisen y-koordinaatti.
        """

        # jos tyhjä laatta eli 0 miinaa avataan kaikki läheiset tyhjät ja numerot
        for tile in self.zeroes:
            if tile.rect.collidepoint(mouse_x, mouse_y):
                self._dfs_open_nearby(mouse_x, mouse_y)
                return

        # laatan avaaminen
        for tile in self.unopened:
            if tile.rect.collidepoint(mouse_x, mouse_y):
                tile.opened = True
                tile.update()
                self.unopened.remove(tile)
                self.opened.add(tile)

    def mark_tile(self, mouse_x, mouse_y):
        """Funktio, joka merkkaa avaamattoman laatan.

        Args:
            mouse_x (float): Hiiren oikean painikkeen painamisen x-koordinaatti.
            mouse_y (float): Hiiren oikean painikkeen painamisen y-koordinaatti.
        """

        if self.unmark_tile(mouse_x, mouse_y):
            return

        # merkkaamattoman merkkaus
        for tile in self.unopened:
            if tile.rect.collidepoint(mouse_x, mouse_y):
                tile.marked = True
                tile.update()
                self.unopened.remove(tile)
                self.marked.add(tile)

    def unmark_tile(self, mouse_x, mouse_y):
        """Funktio, joka poistaa merkin jo merkatusta laatasta.

        Args:
            mouse_x (float): Hiiren oikean painikkeen painamisen x-koordinaatti.
            mouse_y (float): Hiiren oikean painikkeen painamisen y-koordinaatti.

        Returns:
            Bool: Palauttaa True, jos poistettiin merkkaus, jolloin laatalle ei tehdä mitään.
        """

        for tile in self.marked:
            if tile.rect.collidepoint(mouse_x, mouse_y):
                tile.marked = False
                tile.update()
                self.marked.remove(tile)
                self.unopened.add(tile)
                return True

    def mine_opened(self):
        """Funktio, joka kertoo onko mikä tahansa miinoista avattu, jolloin pelaaja häviää pelin.

        Returns:
            Bool: True, jos miina on avattu muuten False.
        """

        for tile in self.opened:
            if len(self._get_colliding_targets(tile, self.mines)) > 0:
                return True
        return False

    def _dfs_open_nearby(self, mouse_x, mouse_y):
        """Rekursiivinen algoritmi, joka aktivoituu, kun pelaaja avaa tyhjän laatan.
        Tällöin avataan kaikki tyhjään laattaan kosketuksissa olevat tyhjät laatat ja
        yksi kerros numeroita tyhjistä laatoista.

        Args:
            mouse_x (float): Hiiren vasemman painikkeen painamisen x-koordinaatti.
            mouse_y (float): Hiiren vasemman painikkeen painamisen y-koordinaatti.
        """

        # ei mennä laudan ulkopuolelle
        if mouse_x<0 or mouse_x>len(self.top_map[0])*self.tile_size:
            return
        if mouse_y<100 or mouse_y>len(self.top_map)*self.tile_size+100:
            return

        # jos miina lopetetaan rekursio
        for mine in self.mines:
            if mine.rect.collidepoint(mouse_x, mouse_y):
                return

        # avataan tyhjästä laatasta vain yksi viereinen numero
        number = False
        for tile in self.numbers_no_zeroes:
            if tile.rect.collidepoint(mouse_x, mouse_y):
                number = True

        # ei avata uudestaan jo avattua laattaa
        opened = False
        for tile in self.opened:
            if tile.rect.collidepoint(mouse_x, mouse_y):
                opened = True

        # laatan avaaminen
        if not opened:
            for tile in self.unopened:
                if tile.rect.collidepoint(mouse_x, mouse_y):
                    tile.opened = True
                    tile.update()
                    self.unopened.remove(tile)
                    self.opened.add(tile)

        # kutsutaan funktiota rekursiivisesti ympärillä oleville laatoille
        if (not opened) and (not number):
            self._dfs_open_nearby(mouse_x, mouse_y-self.tile_size)
            self._dfs_open_nearby(mouse_x, mouse_y+self.tile_size)
            self._dfs_open_nearby(mouse_x-self.tile_size, mouse_y)
            self._dfs_open_nearby(mouse_x+self.tile_size, mouse_y)
            self._dfs_open_nearby(mouse_x-self.tile_size, mouse_y-self.tile_size)
            self._dfs_open_nearby(mouse_x+self.tile_size, mouse_y-self.tile_size)
            self._dfs_open_nearby(mouse_x-self.tile_size, mouse_y+self.tile_size)
            self._dfs_open_nearby(mouse_x+self.tile_size, mouse_y+self.tile_size)

    def is_completed(self):
        """Funktio, joka tarkistaa onko kaikki miinat merkattu ja että onko kaikki ei-miina laatat avattu.

        Returns:
            Bool: Palauttaa True, jos peli on läpäisty eli kaikki ei-miinat on avattu, muuten False.
        """

        if self._all_mines_marked() and self._all_number_tiles_opened():
            return True
        return False

    def _all_mines_marked(self):
        """Tarkistaa onko, jokainen miina merkattu.

        Returns:
            Bool: Jos jokin, miina on merkkaamatta paluttaa False, muuten True.
        """

        for tile in self.marked:
            if len(self._get_colliding_targets(tile, self.mines)) == 0:
                return False
        return True

    def _all_number_tiles_opened(self):
        """Funktio, joka tarkistaa, että kaikki numerolaatat eli ei-miinat on avattu.

        Returns:    
            Bool: Palauttaa False, jos jokin numerolaatoista on avaamatta, muuten True.
        """

        for tile in self.all_number_sprites:
            if len(self._get_colliding_targets(tile, self.opened)) == 0:
                return False
        return True

    def _get_colliding_targets(self, sprite, sprite_group):
        """Funktio, joka kertoo osuuko tietty peliobjekti eli sprite johonki tietyn ryhmän objekteihin.

        Args:
            sprite (pygame.sprite): Peliobjekti, jonka osumista tietyn ryhmän objekteihin tutkitaan.
            sprite_group (pygame.sprite.group()): Peliobjektien joukko.

        Returns:
            int: Palauttaa kuinka moneen joukon objekteista yksittäinen objekti osuu.
        """
        return pygame.sprite.spritecollide(sprite, sprite_group, False)

    def _initialize_lower_layer_sprites(self, lower_map):
        """Funktio, joka alustaa alemman matriisin peliobjektit eli spritet.
        Alempaan matriisiin kuuluu miinat, numerot sekä tyhjät avatut laatat.

        Args:
            lower_map (list): Matriisi, joka kertoo alemman laudan rakenteen. 
            -1 tarkoittaa miinaa, muuten numero kertoo montako miinaa sen ympärillä on.
        """

        width = len(lower_map[0])
        height = len(lower_map)

        for y_coord in range(height):
            for x_coord in range(width):
                tile = lower_map[y_coord][x_coord]
                scale_x = x_coord*self.tile_size
                scale_y = y_coord*self.tile_size+100

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
                    self.mines.add(OpenedTile(scale_x, scale_y, -1))

    def _initialize_top_layer_sprites(self, top_map):
        """Funktio, joka alustaa ylemmän laudan peliobjektit.
        Ylempään lautaan kuuluvat avaamaton, merkattu sekä läpinäkyvä laatta.

        Args:
            top_map (list): Matriisi, joka ilmaisee ylemmän laudan rakenteen.
            (9 tarkoittaa avaamatonta laattaa)
        """
        width = len(top_map[0])
        height = len(top_map)

        for y_coord in range(height):
            for x_coord in range(width):
                scale_x = x_coord*self.tile_size
                scale_y = y_coord*self.tile_size+100
                self.unopened.add(UnopenedTile(scale_x, scale_y))

    def _add_all_sprites(self):
        """Funktio, joka lisää kaikki spritet listaan, jotta piirtäminen näytölle on helpompaa.
        """

        self.all_sprites.add(self.zeroes, self.ones, self.twos, self.threes,
                            self.fours, self.fives, self.sixes, self.sevens,
                            self.eights, self.mines, self.unopened, self.marked)

    def _add_all_numbers(self):
        """Funktio, joka lisää kaikki ei-miinat joukkoon peliobjekteja, jotta voidaan tarkistaa onko peli läpäisty.
        """

        self.all_number_sprites.add(self.zeroes, self.ones, self.twos,
                                    self.threes, self.fours, self.fives,
                                    self.sixes, self.sevens, self.eights)

    def _add_numbers_no_zeroes(self):
        """Funktio, joka lisää kaikki numerot eli ei miinoja eikä nollia peliobjektien listaan,
        jotta _dfs_open_nearby() algoritmi pystyy toteuttamaan rekursion okein
        """
        
        self.numbers_no_zeroes.add(self.ones, self.twos, self.threes,
                                   self.fours, self.fives, self.sixes,
                                   self.sevens, self.eights)
