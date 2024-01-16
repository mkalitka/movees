from movees import db
from movees.api import Api
from movees.server import server
from movees import cli
from movees.utils.format_utils import format_movie, format_person
from movees.config import Config


def add_movie(api, title, year, people):
    """Add a movie to the database."""
    response = api.add_movie(title, year, people)
    print(response["message"])


def list_movies(api):
    """List all movies in the database."""
    response = api.list_movies()
    if response["status_code"] == 200:
        print("Movies:")
        for movie in response["data"]:
            print(format_movie(movie))
    else:
        print(response["message"])


def search_movie(api, title):
    """Search for a movie in the database."""
    response = api.search_movie(title)
    if response["status_code"] == 200:
        print("Movie found:")
        print(format_movie(response["data"]))
    else:
        print(response["message"])


def update_movie(api, title, new_title, year, people):
    """Update a movie in the database."""
    response = api.update_movie(title, new_title, year, people)
    print(response["message"])


def delete_movie(api, title):
    """Delete a movie from the database."""
    response = api.delete_movie(title)
    print(response["message"])


def add_person(api, name):
    """Add a person to the database."""
    response = api.add_person(name)
    print(response["message"])


def list_people(api):
    """List all people in the database."""
    response = api.list_people()
    if response["status_code"] == 200:
        print("People:")
        for person in response["data"]:
            print(format_person(person))
    else:
        print(response["message"])


def search_person(api, name):
    """Search for a person in the database."""
    response = api.search_person(name)
    if response["status_code"] == 200:
        print("Person found:")
        print(format_person(response["data"]))
    else:
        print(response["message"])


def update_person(api, name, new_name):
    """Update a person in the database."""
    response = api.update_person(name, new_name)
    print(response["message"])


def delete_person(api, name):
    """Delete a person from the database."""
    response = api.delete_person(name)
    print(response["message"])


def reset(api):
    """Reset the database."""
    response = api.reset()
    print(response["message"])


def main():
    """Main function."""
    parser = cli.create_parser()
    cmdline_args = parser.parse_args()

    if cmdline_args.subcommand is None:
        parser.print_help()
        return

    config = Config()
    api = None
    remote = False
    host = None
    port = None

    if config.get("remote", "host") != "" and config.get("remote", "port") != "":
        host = config.get("remote", "host")
        port = config.get("remote", "port")
        api = Api(host, port)
        remote = True
    else:
        api = Api()


    if cmdline_args.subcommand == "server":
        print("Starting server...")
        server.run_server(host=cmdline_args.host, port=cmdline_args.port)
    elif cmdline_args.subcommand == "remote":
        if cmdline_args.action == "set":
            config.set("remote", "host", cmdline_args.host)
            config.set("remote", "port", str(cmdline_args.port))
            print("Remote database set.")
        elif cmdline_args.action == "show":
            if remote:
                print(f"Remote database is set to http://{host}:{port}")
            else:
                print("Remote database is not set.")
        elif cmdline_args.action == "unset":
            config.set("remote", "host", "")
            config.set("remote", "port", "")
            print("Remote database unset.")
    else:
        if remote:
            print(f"Using remote database at http://{host}:{port}")

        if cmdline_args.subcommand == "list":
            list_movies(api)
            list_people(api)
        elif cmdline_args.subcommand == "movie":
            if cmdline_args.action == "add":
                add_movie(api, cmdline_args.title, cmdline_args.year, cmdline_args.person)
            elif cmdline_args.action == "list":
                list_movies(api)
            elif cmdline_args.action == "search":
                search_movie(api, cmdline_args.title)
            elif cmdline_args.action == "update":
                update_movie(
                    api,
                    cmdline_args.title,
                    cmdline_args.new_title,
                    cmdline_args.year,
                    cmdline_args.person,
                )
            elif cmdline_args.action == "delete":
                delete_movie(api, cmdline_args.title)
        elif cmdline_args.subcommand == "person":
            if cmdline_args.action == "add":
                add_person(api, cmdline_args.name)
            elif cmdline_args.action == "list":
                list_people(api)
            elif cmdline_args.action == "search":
                search_person(api, cmdline_args.name)
            elif cmdline_args.action == "update":
                update_person(api, cmdline_args.name, cmdline_args.new_name)
            elif cmdline_args.action == "delete":
                delete_person(api, cmdline_args.name)
        elif cmdline_args.subcommand == "reset":
            reset(api)


if __name__ == "__main__":
    main()
