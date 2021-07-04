from enum import Enum

from modules.configs.json_config_parser import JSONFileConfigParser


class ConfigTypes(Enum):
    JSON_PARSER = 1


class ConfigFactory:
    @staticmethod
    def get_default_parser():
        return JSONFileConfigParser()

    @staticmethod
    def get_specific_parser(config_type):
        if ConfigTypes.JSON_PARSER == config_type:
            return JSONFileConfigParser()
