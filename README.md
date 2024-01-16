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

## API

### Movies

#### Add a movie to the database (also add person if doesn't exist)

* Method: **POST**
* Resource: `/movie`
* Arguments:

    * `title` (string)
    * `year` (int)
    * `person` (string, format: "name:role", optional, mutliple)

#### Get information about all movies

* Method: **GET**
* Resource: `/movies`

#### Get information about an movie

* Method: **GET**
* Resource `/movie`
* Arguments:

    * `title` (string)

#### Update information about an movie (also add person if doesn't exist)

* Method: **PUT**
* Resource: `/movie`
* Arguments:

    * `title` (string)
    * `new_title` (string, optional)
    * `year` (int, optional)
    * `person` (string, format: "name:role", optional, multiple

#### Delete a movie from the database

* Method: **DELETE**
* Resource: `/movie`
* Arguments:

    * `title` (string)

#### Add a person to the database

* Method: **POST**
* Resource: `/person`
* Arguments:

    * `name` (string)

#### Get information about all the people

* Method: **GET**
* Resource: `/people`

#### Get information about a person

* Method: **GET**
* Resource: `/person`
* Arguments:

    * `name` (string)

#### Update information about a person

* Method: **PUT**
* Resource: `/person`
* Arguments:

    * `name` (string)
    * `new_name` (string)

#### Delete a person from the database

* Method: **DELETE**
* Resource: `/person`
* Arguments:

    * `name` (string)
