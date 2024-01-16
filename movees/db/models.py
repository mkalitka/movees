import peewee

from movees.db._base import BaseModel


class Movie(BaseModel):
    title = peewee.CharField(unique=True)
    year = peewee.IntegerField()


class Person(BaseModel):
    name = peewee.CharField(unique=True)


class MoviePerson(BaseModel):
    movie = peewee.ForeignKeyField(Movie, backref="people")
    person = peewee.ForeignKeyField(Person, backref="movies")
    role = peewee.CharField()

    class Meta:
        indexes = ((("movie", "person"), True),)
