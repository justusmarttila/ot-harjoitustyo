from tkinter import ttk, constants

class SelectLevelDisplay:
    """Luokka, joka vastaa tasovalintaikkunasta.
    """

    def __init__(self, root, handle_selection, handle_logout):
        """Konstruktori, joka luo uuden tasovalintaikkunan.

        Args:
            root (TKinter-elementti): Pääikkuna, minne näkymä luodaan.
            handle_selection (function): Kutsuttava, kun valitaan taso.
            handle_logout (_type_): Kutsuttava, kun valitaan logout nappi.
        """

        self._root = root
        self._handle_logout = handle_logout
        self._handle_selection = handle_selection
        self._frame = None

        self._init()

    def pack(self):
        """Ikkunan näkymän näyttäminen."""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Sulkee ikkunan näkymän."""

        self._frame.destroy()

    def _beginner_button_handler(self):
        self._handle_selection((9, 9, 10))

    def _intermediate_button_handler(self):
        self._handle_selection((16, 16, 40))

    def _expert_button_handler(self):
        self._handle_selection((30, 16, 99))

    def _init(self):
        """Alusta tasovalintaikkuna"""

        self._frame = ttk.Frame(master=self._root)

        beginner_button = ttk.Button(
            master=self._frame,
            text="Beginner",
            command=self._beginner_button_handler
        )

        intermediate_button = ttk.Button(
            master=self._frame,
            text="Intermediate",
            command=self._intermediate_button_handler
        )

        expert_button = ttk.Button(
            master=self._frame,
            text="Expert",
            command=self._expert_button_handler
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._handle_logout
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=500)

        beginner_button.grid(padx=10, pady=10, sticky=constants.EW)
        intermediate_button.grid(padx=10, pady=10, sticky=constants.EW)
        expert_button.grid(padx=10, pady=10, sticky=constants.EW)
        logout_button.grid(padx=10, pady=10, sticky=constants.EW)
