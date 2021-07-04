from default_config import DEFAULT_JSON_FILE_LOCATION
from modules.configs.config_parser import IConfigParser


class JSONFileConfigParser(IConfigParser):
    def __init__(self):
        self.file_location = DEFAULT_JSON_FILE_LOCATION

    def __init__(self, file_location):
        self.file_location = file_location

    def set_file_location(self, file_location):
        """
        Sets file location of JSON file to parse
        :param file_location: JSON parser
        :return: None
        """
        self.file_location = file_location

    def get_config(self):
        # todo implement
        pass