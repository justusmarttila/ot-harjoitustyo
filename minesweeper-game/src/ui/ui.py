from ui.register_user_display import RegisterUserDispay
from ui.login_display import LoginDisplay
from ui.select_level_display import SelectLevelDisplay

class UI:
    """Pelin käyttöliittymän luokka
    """

    def __init__(self, root):
        """Konstruktori, joka luo uuden käyttöliittymä olion.

        Args:
            root (TKinter-elementti): Pääikkuna, mihin eri näkymät luodaan.
        """

        self._current_display = None
        self._root = root
        self.level = None

    def start(self):
        """Funktio, joka näyttää ensimmäisen näkymän"""

        self._show_login_display()

    def _hide_current_display(self):
        """Piilottaa tällä herkellä näkyvissä olevan näkymän,
        jotta voidaan näyttää jotain muuta.
        """

        if self._current_display:
            self._current_display.destroy()

        self._current_display = None

    def _show_register_user_display(self):
        """Näyttää käyttäjän rekisteröitymisikkunan.
        """

        self._hide_current_display()

        self._current_display = RegisterUserDispay(
            self._root,
            self._show_select_level_display,
            self._show_login_display
        )

        self._current_display.pack()

    def _show_login_display(self):
        """Funktio, joka näyttää kirjautumisnäkymän.
        """

        self._hide_current_display()

        self._current_display = LoginDisplay(
            self._root,
            self._show_select_level_display,
            self._show_register_user_display
        )

        self._current_display.pack()

    def _show_select_level_display(self):
        """Näyttää tasovalintanäkymän.
        """

        self._hide_current_display()

        self._current_display = SelectLevelDisplay(
            self._root,
            self._return_level,
            self._show_login_display)

        self._current_display.pack()

    def _return_level(self, level):
        """Funktio, joka muuttaa valittua tasoa ja sulkee käyttöliittymän.

        Args:
            level (tuple): Tason tiedot muodossa (leveys, korkeus, miinat).
        """
        self.level = level
        self._root.destroy()
        