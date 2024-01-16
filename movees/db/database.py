import os

from movees.db._base import db_file
from movees.db.models import Movie, Person, MoviePerson
from movees.utils import env


DATABASE_PATH = env.get_database_path()


def init():
    db_file.init(DATABASE_PATH)
    db_file.connect()
    db_file.create_tables([Movie, Person, MoviePerson])


def reset():
    db_file.drop_tables([Movie, Person, MoviePerson])
    db_file.create_tables([Movie, Person, MoviePerson])


def close():
    db_file.close()
