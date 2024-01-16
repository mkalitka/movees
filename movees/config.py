import os
import configparser

from movees.utils import env

CONFIG_PATH = env.get_config_path()


_config = configparser.ConfigParser()


def init():
    _config.read(CONFIG_PATH)
    if not _config.has_section("remote"):
        _config.add_section("remote")
    if not _config.has_option("remote", "host"):
        _config.set("remote", "host", "")
    if not _config.has_option("remote", "port"):
        _config.set("remote", "port", "")
    write()


def write():
    with open(CONFIG_PATH, "w+") as f:
        _config.write(f)


def get_config():
    return _config
