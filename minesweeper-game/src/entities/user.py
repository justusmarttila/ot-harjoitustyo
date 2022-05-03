class User:
    """Luokka, joka kuvaa yksittäistä pelaajaa.

    Attributes:
        username: Merkkijonoarvo, joka kuvaa pelaajan käyttäjätunnusta.
        password: Merkkijonoarvo, joka kuvaa käyttäjän salasanaa.
    """

    def __init__(self, username, password):
        """Luokan konstruktori, joka luo uuden käyttäjän.

        Args:
            username: Merkkijonoarvo, joka kuvaa pelaajan käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa käyttäjän salasanaa.
        """

        self.username = username
        self.password = password
        