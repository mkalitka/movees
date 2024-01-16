# movees

#### *A cli database of movies with cli.*

This project was created for **extended Python course** subject.

## Screenshots

**TO-DO**

## Features

- Command line interface
- 2 types of data: movies and people
- Restful API

## Compatibility

This package was tested on Python 3.11, but it should work on Python ^3.8.

## Installation and usage

Please install it with:
```sh
pip3 install -e .
python3 -m movees
```

or use poetry:
```sh
poetry install
poetry run python3 -m movees
```

you can also specify database file path:
```sh
MOVEES_DB_PATH="database.db" python3 -m movees
```
