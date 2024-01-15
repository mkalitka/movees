from enum import Enum


class Message(str, Enum):
    ADD_MOVIE = "Movie %s has been added."
    MOVIE_ALREADY_EXISTS = "Movie %s already exists."
    LIST_MOVIES_PREFIX = "Movies:"
    DISPLAY_MOVIE_PREFIX = "Movie:"
    DISPLAY_MOVIE = "    %s (%s) by %s"
    DISPLAY_MOVIE_NO_PEOPLE = "    %s (%s)"
    UPDATE_MOVIE = "Movie %s has been updated."
    DELETE_MOVIE = "Movie %s has been deleted."
    MOVIE_NOT_FOUND = "Movie %s not found."
    ADD_PERSON = "Person %s has been added."
    PERSON_ALREADY_EXISTS = "Person %s already exists."
    LIST_PEOPLE_PREFIX = "People:"
    DISPLAY_PERSON_PREFIX = "    Person:"
    DISPLAY_PERSON = "        %s"
    DISPLAY_PERSON_MOVIES_PREFIX = "    Movies:"
    DISPLAY_PERSON_MOVIE = "        %s (%s) as %s"
    DISPLAY_PERSON_NO_MOVIES = "        No movies"
    UPDATE_PERSON = "Person %s has been updated."
    DELETE_PERSON = "Person %s has been deleted."
    PERSON_NOT_FOUND = "Person %s not found."

    def __str__(self):
        return self.value
