from tkinter import ttk, StringVar, constants
from services.UI_service import UI_service, InvalidUsernameOrPasswordError

class LoginDisplay:
    """Luokka, joka vastaa Kirjautumisikkunan näyttämisestä.
    """

    def __init__(self, root, handle_login, handle_show_register_display):
        """Konstruktori, jolle annetaan ikkuna mihin piirtää
        sekä kahvat toisiin käyttöliittymän ikkunoihin. Luo uuden kirjautumisikkunan.

        Args:
            root: (TKinter-elementti): Pääikkuna, jonne näkymä luodaan.
            handle_login (function): Kutsuttava funktio, kun käyttäjä kirjautuu.
            handle_show_register_display (function): Siirtyminen rekisteröitymisikkunaan.
        """

        self._root = root
        self._handle_login = handle_login
        self._handle_show_register_display = handle_show_register_display
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

    def _login_handler(self):
        """Funktio, joka kirjaa käyttäjän sisään,
        kun painetaan login-nappulaa.
        Eli UI_servicen kautta tarkistaa onko käyttäjän tiedot syötetty oikein.
        """

        username = self._username_input.get()
        password = self._password_input.get()

        try:
            UI_service.login(username, password)
            self._handle_login()
        except InvalidUsernameOrPasswordError:
            self._display_error("Invalid username or password, try again")


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
        """Funktio, joka alustaa ikkunan näkymät."""

        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=10, pady=10)

        display_label = ttk.Label(master=self._frame, text="Login account")
        display_label.grid(padx=5, pady=5, sticky=constants.W)

        self._initialize_username_slot()
        self._initialize_password_slot()

        register_user_button = ttk.Button(
            master = self._frame,
            text="Register",
            command=self._handle_show_register_display
        )

        login_user_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._login_handler
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=500)

        register_user_button.grid(padx=10, pady=10, sticky=constants.EW)
        login_user_button.grid(padx=10, pady=10, sticky=constants.EW)

        self._hide_error()
