import os
import configparser

from movees.utils import env


class Config:
    def __init__(self, config_path=None):
        self.config_path = config_path or env.get_config_path()
        self._config = configparser.ConfigParser()
        self.load_config()

        if not self._config.has_section("remote") or not self._config.has_option("remote", "host"):
            self.set("remote", "host", "")
        if not self._config.has_section("remote") or not self._config.has_option("remote", "port"):
            self.set("remote", "port", "")

    def load_config(self):
        self._config.read(self.config_path)

    def save_config(self):
        with open(self.config_path, "w+", encoding="utf-8") as config_file:
            self._config.write(config_file)
    
    def get(self, section, option):
        try:
            value = self._config.get(section, option)
        except configparser.NoOptionError:
            value = None
        return value

    def set(self, section, option, value):
        if not self._config.has_section(section):
            self._config.add_section(section)
        self._config.set(section, option, value)
        self.save_config()
