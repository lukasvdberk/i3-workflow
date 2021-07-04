from __future__ import print_function
import json
from types import SimpleNamespace as Namespace

from default_config import DEFAULT_JSON_FILE_LOCATION
from modules.configs.config_parser import IConfigParser


class JSONFileConfigParser(IConfigParser):
    """
    Parses spawner config JSON file and creates objects
    """
    def __init__(self, file_location=DEFAULT_JSON_FILE_LOCATION):
        self.file_location = file_location

    def set_file_location(self, file_location):
        """
        Sets file location of JSON file to parse
        :param file_location: JSON parser
        :return: None
        """
        self.file_location = file_location

    def get_config(self):
        with open(DEFAULT_JSON_FILE_LOCATION, 'r') as json_config_file:
            return json.load(json_config_file, object_hook=lambda d: Namespace(**d))
