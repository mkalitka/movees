import argparse

from movees._version import __version__


def create_parser():
    """Create a parser for the command line arguments."""
    parser = argparse.ArgumentParser(
        prog="movees",
        description="A database of movies, songs and books.",
        epilog="Thank you for using movees!",
    )
    subparsers = parser.add_subparsers(
        dest="subcommand",
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"movees {__version__}",
    )

    # list subparser
    subparsers.add_parser(
        "list",
        help="list all items",
    )

    # movie subparser
    parser_movie = subparsers.add_parser(
        "movie",
        help="manage movies",
    )

    movie_subparsers = parser_movie.add_subparsers(
        dest="action",
        required=True,
    )

    # movie add subparser
    parser_movie_add = movie_subparsers.add_parser(
        "add",
        help="add a new movie",
    )

    parser_movie_add.add_argument(
        "-t",
        "--title",
        required=True,
        help="title of the movie",
    )

    parser_movie_add.add_argument(
        "-y",
        "--year",
        required=True,
        type=int,
        help="year of publication of the movie",
    )

    parser_movie_add.add_argument(
        "-p",
        "--person",
        nargs=2,
        action="append",
        metavar=("NAME", "ROLE"),
        help="people involved in the movie",
    )

    # movie list subparser
    movie_subparsers.add_parser(
        "list",
        help="list all movies",
    )

    # movie search subparser
    parser_movie_search = movie_subparsers.add_parser(
        "search",
        help="search for a movie",
    )

    parser_movie_search.add_argument(
        "-t",
        "--title",
        required=True,
        help="title of the movie",
    )

    # movie update subparser
    parser_movie_update = movie_subparsers.add_parser(
        "update",
        help="update a movie",
    )

    parser_movie_update.add_argument(
        "-t",
        "--title",
        required=True,
        help="title of the movie",
    )

    parser_movie_update.add_argument(
        "-n",
        "--new-title",
        help="new title of the movie",
    )

    parser_movie_update.add_argument(
        "-y",
        "--year",
        type=int,
        help="year of publication of the movie",
    )

    parser_movie_update.add_argument(
        "-p",
        "--person",
        nargs=2,
        action="append",
        metavar=("NAME", "ROLE"),
        help="people involved in the movie",
    )

    # movie delete subparser
    parser_movie_delete = movie_subparsers.add_parser(
        "delete",
        help="delete a movie",
    )

    parser_movie_delete.add_argument(
        "-t",
        "--title",
        required=True,
        help="title of the movie",
    )

    # person subparser
    parser_person = subparsers.add_parser(
        "person",
        help="manage people",
    )

    person_subparsers = parser_person.add_subparsers(
        dest="action",
        required=True,
    )

    # person add subparser
    parser_person_add = person_subparsers.add_parser(
        "add",
        help="add a new person",
    )

    parser_person_add.add_argument(
        "-n",
        "--name",
        required=True,
        help="name of the person",
    )

    # person list subparser
    person_subparsers.add_parser(
        "list",
        help="list all people",
    )

    # person search subparser
    parser_person_search = person_subparsers.add_parser(
        "search",
        help="search for a person",
    )

    parser_person_search.add_argument(
        "-n",
        "--name",
        required=True,
        help="name of the person",
    )

    # person update subparser
    parser_person_update = person_subparsers.add_parser(
        "update",
        help="update a person",
    )

    parser_person_update.add_argument(
        "-n",
        "--name",
        required=True,
        help="name of the person",
    )

    parser_person_update.add_argument(
        "-m",
        "--new-name",
        help="new name of the person",
    )

    # person delete subparser
    parser_person_delete = person_subparsers.add_parser(
        "delete",
        help="delete a person",
    )

    parser_person_delete.add_argument(
        "-n",
        "--name",
        required=True,
        help="name of the person",
    )

    # reset subparser
    subparsers.add_parser(
        "reset",
        help="reset the database",
    )

    # server subparser
    parser_server = subparsers.add_parser(
        "server",
        help="start the server",
    )

    parser_server.add_argument(
        "-H",
        "--host",
        default="0.0.0.0",
        help="host to run the server on",
    )

    parser_server.add_argument(
        "-p",
        "--port",
        type=int,
        default=5000,
        help="port to run the server on",
    )

    return parser
