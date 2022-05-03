from pathlib import Path
from entities import score
from repositories import user_repository
from config import SCORES_FILE_PATH

class ScoreRepository:

    def __init__(self, file_path):

        self._file_path = file_path

    def fetch_all(self):
        return self._read()

    def clear_all(self):
        self._write([])

    def fetch_by_username(self, username):
        scores = self.fetch_all()
        user_scores = filter(
            lambda score: score.user and score.user.username == username, scores)

        return list(user_scores)

    def set_score(self, score):

        scores = self.fetch_all()
        scores.append(score)
        self._write(scores)
        return score

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def _read(self):
        scores = []

        self._ensure_file_exists()

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")

                score_id = parts[0]
                username = parts[1]
                time = parts[2]

                user = user_repository.fetch_by_username(
                    username) if username else None

                scores.append(score(user, time, score_id))

        return scores

    def _write(self, scores):
        self._ensure_file_exists()

        with open(self._file_path, "w", encoding="utf-8") as file:
            for score in scores:
                username = score.user.username if score.user else ""

                row = f"{score.id};{username};{score.time}"

                file.write(row+"\n")

score_repo = ScoreRepository(SCORES_FILE_PATH)
