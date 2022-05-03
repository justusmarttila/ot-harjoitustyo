from tkinter import ttk, constants

class SelectLevelDisplay:

    def __init__(self, root, handle_logout):

        self._root = root
        self._handle_logout = handle_logout
        self.level = None
        self._frame = None

        self._init()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _beginner_button_handler(self):
        self.level = (9, 9, 10)
        self._root.quit()

    def _intermediate_button_handler(self):
        self.level = (16, 16, 40)
        self._root.quit()

    def _expert_button_handler(self):
        self.level = (16, 30, 99)
        self._root.quit()

    def _init(self):
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
