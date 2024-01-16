import requests

from movees import db
from movees.db import crud
from movees.responses.generic import generic
from movees.responses.errors import not_found, service_unavailable
from movees.responses import Message


class Api:
    def __init__(self, host=None, port=None):
        self.host = host
        self.port = port
        self.api_key = None
        self.remote = False if host is None else True
        if not self.remote:
            db.init()


    def _create_response(self, response):
        try:
            status_code = response["status_code"]
        except KeyError:
            return not_found()

        try:
            data = response["data"]
        except KeyError:
            data = None

        try:
            message = response["message"]
        except KeyError:
            message = None

        return generic(status_code, data=data, message=message)

    def _get(self, path):
        try:
            return self._create_response(
                requests.get(
                    f"http://{self.host}:{self.port}{path}",
                ).json()
            )
        except requests.exceptions.ConnectionError:
            return service_unavailable()

    def _post(self, path):
        try:
            return self._create_response(
                requests.post(
                    f"http://{self.host}:{self.port}{path}",
                ).json()
            )
        except requests.exceptions.ConnectionError:
            return service_unavailable()


    def _put(self, path):
        try:
            return self._create_response(
                requests.put(
                    f"http://{self.host}:{self.port}{path}",
                ).json()
            )
        except requests.exceptions.ConnectionError:
            return service_unavailable()

    def _delete(self, path):
        try:
            return self._create_response(
                requests.delete(
                    f"http://{self.host}:{self.port}{path}",
                ).json()
            )
        except requests.exceptions.ConnectionError:
            return service_unavailable()

    def add_movie(self, title, year, people):
        if self.remote:
            if people is None:
                return self._post(f"/movie?title={title}&year={year}")
            else:
                people = [":".join(person) for person in people]
                people_arg = ""
                for person in people:
                    people_arg += f"&person={person}"
                return self._post(f"/movie?title={title}&year={year}{people_arg}")
        else:
            return crud.add_movie(title, year, people)

    def list_movies(self):
        if self.remote:
            return self._get("/movies")
        else:
            return crud.list_movies()

    def search_movie(self, title):
        if self.remote:
            return self._get(f"/movie?title={title}")
        else:
            return crud.search_movie(title)

    def update_movie(self, title, new_title, year, people):
        if self.remote:
            new_title_arg = "" if new_title is None else f"&new_title={new_title}"
            year_arg = "" if year is None else f"&year={year}"
            people_arg = ""
            if people is not None:
                people = [":".join(person) for person in people]
                for person in people:
                    people_arg += f"&person={person}"
            return self._put(
                f"/movie?title={title}{new_title_arg}{year_arg}{people_arg}"
            )
        else:
            return crud.update_movie(title, new_title, year, people)

    def delete_movie(self, title):
        if self.remote:
            return self._delete(f"/movie?title={title}")
        else:
            return crud.delete_movie(title)

    def add_person(self, name):
        if self.remote:
            return self._post(f"/person?name={name}")
        else:
            return crud.add_person(name)

    def list_people(self):
        if self.remote:
            return self._get("/people")
        else:
            return crud.list_people()

    def search_person(self, name):
        if self.remote:
            return self._get(f"/person?name={name}")
        else:
            return crud.search_person(name)

    def update_person(self, name, new_name):
        if self.remote:
            return self._put(f"/person?name={name}&new_name={new_name}")
        else:
            return crud.update_person(name, new_name)

    def delete_person(self, name):
        if self.remote:
            return self._delete(f"/person?name={name}")
        else:
            return crud.delete_person(name)

    def reset(self):
        if self.remote:
            return self._post("/reset")
        else:
            return crud.reset()
