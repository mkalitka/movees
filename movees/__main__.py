from movees import db
from movees.db import crud
from movees import api
from movees.api import server
from movees import cli
from movees.utils.format_utils import format_movie, format_person


def add_movie(title, year, people):
    """Add a movie to the database."""
    response = crud.add_movie(title, year, people)
    print(response["message"])


def list_movies():
    """List all movies in the database."""
    response = crud.list_movies()
    print("Movies:")
    for movie in response["data"]:
        print(format_movie(movie))


def search_movie(title):
    """Search for a movie in the database."""
    response = crud.search_movie(title)
    print("Movie found:")
    print(format_movie(response["data"]))


def update_movie(title, new_title, year, people):
    """Update a movie in the database."""
    response = crud.update_movie(title, new_title, year, people)
    print(response["message"])


def delete_movie(title):
    """Delete a movie from the database."""
    response = crud.delete_movie(title)
    print(response["message"])


def add_person(name):
    """Add a person to the database."""
    response = crud.add_person(name)
    print(response["message"])


def list_people():
    """List all people in the database."""
    response = crud.list_people()
    print("People:")
    for person in response["data"]:
        print(format_person(person))


def search_person(name):
    """Search for a person in the database."""
    response = crud.search_person(name)
    print("Person found:")
    print(format_person(response["data"]))


def update_person(name, new_name):
    """Update a person in the database."""
    response = crud.update_person(name, new_name)
    print(response["message"])


def delete_person(name):
    """Delete a person from the database."""
    response = crud.delete_person(name)
    print(response["message"])


def main():
    """Main function."""
    parser = cli.create_parser()
    cmdline_args = parser.parse_args()

    if cmdline_args.subcommand is None:
        parser.print_help()
        return

    db.init()

    if cmdline_args.subcommand == "list":
        list_movies()
        list_people()

    elif cmdline_args.subcommand == "movie":
        if cmdline_args.action == "add":
            add_movie(cmdline_args.title, cmdline_args.year, cmdline_args.person)
        elif cmdline_args.action == "list":
            list_movies()
        elif cmdline_args.action == "search":
            search_movie(cmdline_args.title)
        elif cmdline_args.action == "update":
            update_movie(
                cmdline_args.title,
                cmdline_args.new_title,
                cmdline_args.year,
                cmdline_args.person,
            )
        elif cmdline_args.action == "delete":
            delete_movie(cmdline_args.title)

    elif cmdline_args.subcommand == "person":
        if cmdline_args.action == "add":
            add_person(cmdline_args.name)
        elif cmdline_args.action == "list":
            list_people()
        elif cmdline_args.action == "search":
            search_person(cmdline_args.name)
        elif cmdline_args.action == "update":
            update_person(cmdline_args.name, cmdline_args.new_name)
        elif cmdline_args.action == "delete":
            delete_person(cmdline_args.name)

    elif cmdline_args.subcommand == "reset":
        db.reset()

    elif cmdline_args.subcommand == "server":
        server.run_server(host=cmdline_args.host, port=cmdline_args.port)

    db.close()


if __name__ == "__main__":
    main()
