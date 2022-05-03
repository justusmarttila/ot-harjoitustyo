import uuid

class Score:

    def __init__(self, time, user=None, score_id=None):
        self.time = time
        self.user = user
        self.id = score_id or str(uuid.uuid4())

        