import os

from movees.db._base import db_file
from movees.db.models import Movie, Person, MoviePerson


if os.environ.get("MOVEES_DB_PATH"):
    DATABASE_PATH = os.environ["MOVEES_DB_PATH"]
else:
    if os.name == "nt":
        DATABASE_PATH = os.path.join(os.environ["APPDATA"], "movees", "database.db")
    else:
        DATABASE_PATH = os.path.join(
            os.environ["HOME"], ".local", "share", "movees", "database.db"
        )

os.makedirs(os.path.dirname(os.path.abspath(DATABASE_PATH)), exist_ok=True)


def init():
    db_file.init(DATABASE_PATH)
    db_file.connect()
    db_file.create_tables([Movie, Person, MoviePerson])


def close():
    db_file.close()
