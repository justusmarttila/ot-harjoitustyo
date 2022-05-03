from tkinter import ttk, StringVar, constants

class LoginDisplay:

    def __init__(self, root, handle_login, handle_show_register_user_display):

        self._root = root
        self._handle_login = handle_login
        self._handle_show_register_user_display = handle_show_register_user_display
        self._username_input = None
        self._password_input = None
        self._frame = None
        self._error_variable = None
        self._error_label = None

        self._init()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _display_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _login_handler(self):
        username = self._username_input.get()
        password = self._password_input.get()

        self._handle_login()


    def _initialize_username_slot(self):
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_input = ttk.Entry(master=self._frame)

        username_label.grid(padx=10, pady=10, sticky=constants.W)
        self._username_input.grid(padx=10, pady=10, sticky=constants.EW)

    def _initialize_password_slot(self):
        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_input = ttk.Entry(master=self._frame)

        password_label.grid(padx=10, pady=10, sticky=constants.W)
        self._password_input.grid(padx=10, pady=10, sticky=constants.EW)

    def _init(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(master=self._frame, textvariable=self._error_variable, foreground="red")

        self._error_label.grid(padx=10, pady=10)

        self._initialize_username_slot()
        self._initialize_password_slot()

        register_user_button = ttk.Button(
            master = self._frame,
            text="Register",
            command=self._handle_show_register_user_display
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
