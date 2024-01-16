import os


def get_config_path():
    path = None

    if os.environ.get("MOVEES_CONFIG"):
        path = os.environ["MOVEES_CONFIG"]
    else:
        if os.name == "nt":
            path = os.path.join(os.environ["APPDATA"], "movees", "config.ini")
        else:
            path = os.path.join(os.environ["HOME"], ".config", "movees", "config.ini")

    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path


def get_database_path():
    path = None

    if os.environ.get("MOVEES_DB_PATH"):
        path = os.environ["MOVEES_DB_PATH"]
    else:
        if os.name == "nt":
            path = os.path.join(os.environ["APPDATA"], "movees", "database.db")
        else:
            path = os.path.join(os.environ["HOME"], ".local", "share", "movees", "database.db")

    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path
