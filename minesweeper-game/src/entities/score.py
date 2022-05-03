import uuid

class Score:

    def __init__(self, user=None, time=0, score_id=None):
        self.user = user
        self.time = time
        self.id = score_id or str(uuid.uuid4())
      