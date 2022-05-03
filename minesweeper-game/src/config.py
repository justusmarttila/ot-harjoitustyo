import os

dirname = os.path.dirname(__file__)

SCORES_FILENAME = os.getenv("SCORES_FILENAME") or "scores.csv"
SCORES_FILE_PATH = os.path.join(dirname, "..", "data", SCORES_FILENAME)

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)