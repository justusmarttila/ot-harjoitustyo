from ui.register_user_display import RegisterUserDispay
from ui.login_display import LoginDisplay
from ui.select_level_display import SelectLevelDisplay


class UI:
    """Pelin käyttöliittymän luokka"""

    def __init__(self, root):
        self._current_display = None
        self._root = root
        self.level = None
        
    def start(self):

        self._show_login_display()

    def _hide_current_display(self):
        if self._current_display:
            self._current_display.destroy()

        self._current_display = None

    def _show_register_user_display(self):
        self._hide_current_display()

        self._current_display = RegisterUserDispay(
            self._root,
            self._show_select_level_display,
            self._show_login_display
        )

        self._current_display.pack()

    def _show_login_display(self):
        self._hide_current_display()

        self._current_display = LoginDisplay(
            self._root,
            self._show_select_level_display,
            self._show_register_user_display
        )

        self._current_display.pack()
        
    def _show_select_level_display(self):
        self._hide_current_display()
        
        self._current_display = SelectLevelDisplay(self._root, self._return_level, self._show_login_display)

        self._current_display.pack()

    def _return_level(self, level):
        self.level = level
        self._root.destroy()