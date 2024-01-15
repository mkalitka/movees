from peewee import DoesNotExist, IntegrityError

from movees import db
from movees import cli
from movees.responses.client import Message


def add_movie(title, year, people):
    """Add a movie to the database."""
    try:
        db.add_movie(title, year, people)
        print(Message.ADD_MOVIE % title)
    except IntegrityError:
        print(Message.MOVIE_ALREADY_EXISTS % title)


def list_movies():
    """List all movies in the database."""
    print(Message.LIST_MOVIES_PREFIX)
    movies = db.list_movies()
    for movie in movies:
        if len(movie.people) == 0:
            print(Message.DISPLAY_MOVIE_NO_PEOPLE % (movie.title, movie.year))
        else:
            people = ""
            for person in movie.people:
                people += f"{person.person.name} ({person.role}), "
            people = people[:-2]
            print(Message.DISPLAY_MOVIE % (movie.title, movie.year, people))


def search_movie(title):
    """Search for a movie in the database."""
    try:
        movie = db.search_movie(title)
        people = ""
        for person in movie.people:
            people += f"{person.person.name} ({person.role}), "
        people = people[:-2]
        print(Message.DISPLAY_MOVIE % (movie.title, movie.year, people))
    except DoesNotExist:
        print(Message.MOVIE_NOT_FOUND % title)


def update_movie(title, new_title, year, people):
    """Update a movie in the database."""
    try:
        db.update_movie(title, new_title, year, people)
        print(Message.UPDATE_MOVIE % title)
    except DoesNotExist:
        print(Message.MOVIE_NOT_FOUND % title)


def delete_movie(title):
    """Delete a movie from the database."""
    try:
        db.delete_movie(title)
        print(Message.DELETE_MOVIE % title)
    except DoesNotExist:
        print(Message.MOVIE_NOT_FOUND % title)


def add_person(name):
    """Add a person to the database."""
    try:
        db.add_person(name)
        print(Message.ADD_PERSON % name)
    except IntegrityError:
        print(Message.PERSON_ALREADY_EXISTS % name)


def list_people():
    """List all people in the database."""
    print(Message.LIST_PEOPLE_PREFIX)
    people = db.list_people()
    for person in people:
        print(Message.DISPLAY_PERSON_PREFIX)
        print(Message.DISPLAY_PERSON % person.name)
        print(Message.DISPLAY_PERSON_MOVIES_PREFIX)
        if len(person.movies) == 0:
            print(Message.DISPLAY_PERSON_NO_MOVIES)
        else:
            for movie in person.movies:
                print(
                    Message.DISPLAY_PERSON_MOVIE
                    % (movie.movie.title, movie.movie.year, movie.role)
                )


def search_person(name):
    """Search for a person in the database."""
    try:
        person = db.search_person(name)
        print(Message.DISPLAY_PERSON_PREFIX)
        print(Message.DISPLAY_PERSON % person.name)
        print(Message.DISPLAY_PERSON_MOVIES_PREFIX)
        if len(person.movies) == 0:
            print(Message.DISPLAY_PERSON_NO_MOVIES)
        else:
            for movie in person.movies:
                print(
                    Message.DISPLAY_PERSON_MOVIE
                    % (movie.movie.title, movie.movie.year, movie.role)
                )
    except DoesNotExist:
        print(Message.PERSON_NOT_FOUND % name)


def update_person(name, new_name):
    """Update a person in the database."""
    try:
        db.update_person(name, new_name)
        print(Message.UPDATE_PERSON % name)
    except DoesNotExist:
        print(Message.PERSON_NOT_FOUND % name)


def delete_person(name):
    """Delete a person from the database."""
    try:
        db.delete_person(name)
        print(Message.DELETE_PERSON % name)
    except DoesNotExist:
        print(Message.PERSON_NOT_FOUND % name)


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

    db.close()


if __name__ == "__main__":
    main()
