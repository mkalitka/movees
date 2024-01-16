from movees import db
from movees.api import Api
from movees.server import server
from movees import cli
from movees.utils.format_utils import format_movie, format_person
from movees import config


def add_movie(api, title, year, people):
    """Add a movie to the database."""
    response = api.add_movie(title, year, people)
    print(response["message"])


def list_movies(api):
    """List all movies in the database."""
    response = api.list_movies()
    print("Movies:")
    for movie in response["data"]:
        print(format_movie(movie))


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
    print("People:")
    for person in response["data"]:
        print(format_person(person))


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


def main():
    """Main function."""
    parser = cli.create_parser()
    cmdline_args = parser.parse_args()

    if cmdline_args.subcommand is None:
        parser.print_help()
        return

    config.init()

    api = None
    remote = False
    conf = config.get_config()

    if (
        conf.has_option("remote", "host")
        and conf.has_option("remote", "port")
        and not conf.get("remote", "host") == ""
        and not conf.get("remote", "port") == ""
    ):
        host = conf.get("remote", "host")
        port = conf.get("remote", "port")
        api = Api(host, port)
        print(f"Using remote database at http://{host}:{port}")
        remote = True
    else:
        api = Api()
        db.init()

    if cmdline_args.subcommand == "server":
        print("Starting server...")
        server.run_server(host=cmdline_args.host, port=cmdline_args.port)

    elif cmdline_args.subcommand == "remote":
        if cmdline_args.clear:
            conf.set("remote", "host", "")
            conf.set("remote", "port", "")
            config.write()
            print("Remote database cleared.")
        else:
            if cmdline_args.host is None or cmdline_args.port is None:
                parser.print_help()
                return
            else:
                conf.set("remote", "host", cmdline_args.host)
                conf.set("remote", "port", str(cmdline_args.port))
                config.write()
                print(f"Remote database set to http://{cmdline_args.host}:{cmdline_args.port}")

    elif cmdline_args.subcommand == "list":
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
        if remote:
            print("Cannot reset remote database.")
        else:
            db.reset()

    if not remote:
        db.close()


if __name__ == "__main__":
    main()
