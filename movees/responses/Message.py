from enum import Enum


class Message(str, Enum):
    ADD_MOVIE = "Movie %s has been added."
    DELETE_MOVIE = "Movie %s has been deleted."
    UPDATE_MOVIE = "Movie %s has been updated."
    ADD_PERSON = "Person %s has been added."
    DELETE_PERSON = "Person %s has been deleted."
    UPDATE_PERSON = "Person %s has been updated."

    MOVIE_ALREADY_EXISTS = "Movie %s already exists."
    MOVIE_NOT_FOUND = "Movie %s not found."
    PERSON_ALREADY_EXISTS = "Person %s already exists."
    PERSON_NOT_FOUND = "Person %s not found."

    def __str__(self):
        return self.value
