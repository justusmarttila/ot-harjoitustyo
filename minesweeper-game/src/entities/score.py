import uuid

class Score:
    """Luokka, joka kuvaa yksittäistä pelin läpipelaamista
    
    Attributes:
        user: User-olio, joka kuvaa suorituksen tekijää
        time: Float-arvo, joka kuvaa suoritukseen kulunutta aikaa
        score_id: Integer-arvo, joka kuvaa suorituksen id:tä
    """

    def __init__(self, user=None, time=0, score_id=None):
        self.user = user
        self.time = time
        self.id = score_id or str(uuid.uuid4())
      