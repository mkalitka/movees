from peewee import DoesNotExist, IntegrityError

from movees.db import Movie, Person, MoviePerson
from movees.responses import Message
from movees.responses import successes, errors


def _get_movie_data(title):
    movie = Movie.get(Movie.title == title)
    return {
        "movie": {
            "title": movie.title,
            "year": movie.year,
            "people": [
                {"name": person.person.name, "role": person.role}
                for person in MoviePerson.select().where(MoviePerson.movie == movie)
            ],
        }
    }


def _get_person_data(name):
    person = Person.get(Person.name == name)
    return {
        "person": {
            "name": person.name,
            "movies": [
                {
                    "title": movie.movie.title,
                    "year": movie.movie.year,
                    "role": movie.role,
                }
                for movie in MoviePerson.select().where(MoviePerson.person == person)
            ],
        }
    }


def add_movie(title, year, people):
    try:
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
        return successes.added(
            message=(Message.ADD_MOVIE % title), item=_get_movie_data(title)
        )
    except IntegrityError:
        return errors.already_exists(message=(Message.MOVIE_ALREADY_EXISTS % title))
    except Exception as e:
        return errors.error(e)


def list_movies():
    items = [_get_movie_data(movie.title) for movie in Movie.select()]
    return successes.listed(items=items)


def search_movie(title):
    try:
        return successes.found(item=_get_movie_data(title))
    except DoesNotExist:
        return errors.not_found(message=(Message.MOVIE_NOT_FOUND % title))
    except Exception as e:
        return errors.error(e)


def update_movie(title, new_title, year, people):
    try:
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
        return successes.updated(
            message=(Message.UPDATE_MOVIE % title), item=_get_movie_data(movie.title)
        )
    except DoesNotExist:
        return errors.not_found(message=(Message.MOVIE_NOT_FOUND % title))
    except Exception as e:
        return errors.error(e)


def delete_movie(title):
    try:
        item = _get_movie_data(title)
        movie = Movie.get(Movie.title == title)
        for movieperson in MoviePerson.select().where(MoviePerson.movie == movie):
            movieperson.delete_instance()
        movie.delete_instance()
        return successes.deleted(message=(Message.DELETE_MOVIE % title), item=item)
    except DoesNotExist:
        return errors.not_found(message=(Message.MOVIE_NOT_FOUND % title))


def add_person(name):
    try:
        person = Person.create(name=name)
        person.save()
        return successes.added(
            message=(Message.ADD_PERSON % name), item=_get_person_data(name)
        )
    except IntegrityError:
        return errors.already_exists(message=(Message.PERSON_ALREADY_EXISTS % name))
    except Exception as e:
        return errors.error(e)


def list_people():
    return successes.listed(
        items=[_get_person_data(person.name) for person in Person.select()]
    )


def search_person(name):
    try:
        return successes.found(item=_get_person_data(name))
    except DoesNotExist:
        return errors.not_found(message=(Message.PERSON_NOT_FOUND % name))
    except Exception as e:
        return errors.error(e)


def update_person(name, new_name):
    try:
        person = Person.get(Person.name == name)
        person.name = new_name
        person.save()
        return successes.updated(
            message=(Message.UPDATE_PERSON % name), item=_get_person_data(person.name)
        )
    except DoesNotExist:
        return errors.not_found(message=(Message.PERSON_NOT_FOUND % name))
    except Exception as e:
        return errors.error(e)


def delete_person(name):
    try:
        item = _get_person_data(name)
        person = Person.get(Person.name == name)
        for movieperson in MoviePerson.select().where(MoviePerson.person == person):
            movieperson.delete_instance()
        person.delete_instance()
        return successes.deleted(message=(Message.DELETE_PERSON % name), item=item)
    except DoesNotExist:
        return errors.not_found(message=(Message.PERSON_NOT_FOUND % name))
    except Exception as e:
        return errors.error(e)
