from modules.configs.config_parser import IConfigParser


class JSONFileConfigParser(IConfigParser):
    def __init__(self, file_location):
        self.file_location = file_location

    def get_config(self):
        # todo implement
        pass