from tkinter import ttk, StringVar, constants
from services.UI_service import UI_service, UsernameAlreadyExistsError

class RegisterUserDispay:
    """Luokka, joka vastaa rekisteröitymismisikkunan näyttämisestä.
    """

    def __init__(self, root, handle_register_user, handle_show_login_display):
        """Konstruktori, joka luo uuden rekisteröitymisikkunan.

        Args:
            root (TKinter-elementti): Pääikkuna, minne ikkuna piirretään.
            handle_register_user (function): Kutsuttava, kun painetaan register.
            handle_show_login_display (function): Kutsuttava, kun painetaan login.
        """

        self._root = root
        self._handle_register_user = handle_register_user
        self._handle_show_login_display = handle_show_login_display
        self._username_input = None
        self._password_input = None
        self._frame = None
        self._error_variable = None
        self._error_label = None

        self._init()

    def pack(self):
        """Ikkunan näkymän näyttäminen."""

        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Sulkee ikkunan näkymän."""

        self._frame.destroy()

    def _display_error(self, message):
        """Funktio, joka vastaa virhe viestin asettamisesta.

        Args:
            message (Str): Virheviesti.
        """

        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        """Funktio, joka poistaa virheviestin ikkunasta."""

        self._error_label.grid_remove()

    def _register_user_handler(self):
        """Funktio, joka vastaa käyttäjän rekisteröimisestä tarkistamalla,
        että annetut tiedot ovat kelvolliset ja lisäämällä UI_servicen
        kautta tiedot tietokantaan.
        """

        username = self._username_input.get()
        password = self._password_input.get()

        if len(password) == 0 or len(username) == 0:
            self._display_error("Username and password is required")
            return
        if len(username) < 3:
            self._display_error("Username must be atleast 3 characters")
            return

        try:
            UI_service.register_user(username, password)
            self._handle_register_user()
        except UsernameAlreadyExistsError:
            self._display_error("This username already exists, try again")

    def _initialize_username_slot(self):
        """Funktio, joka alustaa käyttäjänimen syöttämista varten olevan kentän."""

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_input = ttk.Entry(master=self._frame)
        username_label.grid(padx=10, pady=10, sticky=constants.W)
        self._username_input.grid(padx=10, pady=10, sticky=constants.EW)

    def _initialize_password_slot(self):
        """Funktio, joka alustaa salasanan syöttämiseen tarkoitetun kentän."""

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_input = ttk.Entry(master=self._frame)
        password_label.grid(padx=10, pady=10, sticky=constants.W)
        self._password_input.grid(padx=10, pady=10, sticky=constants.EW)

    def _init(self):
        """Funktio, joka alustaa rekisteröitymisikkunan näkymät."""

        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=10, pady=10)

        display_label = ttk.Label(master=self._frame, text="Register account")
        display_label.grid(padx=5, pady=5, sticky=constants.W)

        self._initialize_username_slot()
        self._initialize_password_slot()

        register_user_button = ttk.Button(
            master=self._frame,
            text="Register",
            command=self._register_user_handler
        )

        login_user_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._handle_show_login_display
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=500)

        register_user_button.grid(padx=10, pady=10, sticky=constants.EW)
        login_user_button.grid(padx=10, pady=10, sticky=constants.EW)

        self._hide_error()
        