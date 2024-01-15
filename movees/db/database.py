from movees.db._base import db_file
from movees.db.models import Movie, Person, MoviePerson

DATABASE_PATH = "database.db"


def init():
    db_file.init(DATABASE_PATH)
    db_file.connect()
    db_file.create_tables([Movie, Person, MoviePerson])


def close():
    db_file.close()
