from typing import List

import fastapi
import uvicorn


from movees.db import crud
from movees.api.response import create_json_response
from movees.responses.successes import success
from movees.responses.errors import not_found, invalid, invalid_method

app = fastapi.FastAPI(default_response_class=fastapi.responses.JSONResponse)


@app.exception_handler(fastapi.exceptions.RequestValidationError)
async def validation_exception_handler(request, exc):
    return create_json_response(invalid(data=exc.errors()))


@app.exception_handler(404)
async def not_found_handler(request, exc):
    return create_json_response(not_found(message="Not found"))


@app.exception_handler(405)
async def method_not_allowed_handler(request, exc):
    return create_json_response(invalid_method(message="Method not allowed"))


@app.get("/")
@app.get("/status")
async def status():
    return create_json_response(success(data={"status": "ok"}))


@app.post("/movie")
async def add_movie(title, year, person: List[str] = fastapi.Query(None)):
    people = person
    if people:
        people = [p.split(":") for p in people]
        for person in people:
            if len(person) != 2:
                return create_json_response(invalid(message="Invalid person format"))
    return create_json_response(crud.add_movie(title, year, people))


@app.get("/movies")
async def list_movies():
    return create_json_response(crud.list_movies())


@app.get("/movie")
async def search_movie(title):
    return create_json_response(crud.search_movie(title))


@app.put("/movie")
async def update_movie(
    title, new_title=None, year=None, person: List[str] = fastapi.Query(None)
):
    people = person
    if people:
        people = [p.split(":") for p in people]
        for person in people:
            if len(person) != 2:
                return create_json_response(invalid(message="Invalid person format"))
    return create_json_response(crud.update_movie(title, new_title, year, people))


@app.delete("/movie")
async def delete_movie(title):
    return create_json_response(crud.delete_movie(title))


@app.post("/person")
async def add_person(name):
    return create_json_response(crud.add_person(name))


@app.get("/people")
async def list_people():
    return create_json_response(crud.list_people())


@app.get("/person")
async def search_person(name):
    return create_json_response(crud.search_person(name))


@app.put("/person")
async def update_person(name, new_name):
    return create_json_response(crud.update_person(name, new_name))


@app.delete("/person")
async def delete_person(name):
    return create_json_response(crud.delete_person(name))


def run_server(host="0.0.0.0", port=5000):
    uvicorn.run(app, host=host, port=port)
