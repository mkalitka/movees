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
        indexes = (
            (("movie", "person"), True),
        )


def add_movie(title, year, people):
    movie = Movie.create(title=title, year=year)
    if people is not None:
        for person in people:
            new_person = Person.get_or_create(name=person[0])[0]
            movieperson = MoviePerson.get_or_create(
                movie=movie, person=new_person, role=person[1]
            )[0]
            new_person.save()
            movieperson.save()
    movie.save()


def list_movies():
    return Movie.select()


def search_movie(title):
    return Movie.get(Movie.title == title)


def update_movie(title, new_title, year, people):
    movie = Movie.get(Movie.title == title)
    if new_title is not None:
        movie.title = new_title
    if year is not None:
        movie.year = year
    if people is not None:
        for movieperson in MoviePerson.select().where(MoviePerson.movie == movie):
            movieperson.delete_instance()
        for person in people:
            new_person = Person.get_or_create(name=person[0])[0]
            movieperson = MoviePerson.create(
                movie=movie, person=new_person, role=person[1]
            )
            new_person.save()
            movieperson.save()
    movie.save()


def delete_movie(title):
    movie = Movie.get(Movie.title == title)
    for movieperson in MoviePerson.select().where(MoviePerson.movie == movie):
        movieperson.delete_instance()
    movie.delete_instance()


def add_person(name):
    person = Person.create(name=name)
    person.save()


def list_people():
    return Person.select()


def search_person(name):
    return Person.get(Person.name == name)


def update_person(name, new_name):
    person = Person.get(Person.name == name)
    person.name = new_name
    person.save()


def delete_person(name):
    person = Person.get(Person.name == name)
    for movieperson in MoviePerson.select().where(MoviePerson.person == person):
        movieperson.delete_instance()
    person.delete_instance()
