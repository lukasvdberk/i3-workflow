import json
from default_config import DEFAULT_JSON_FILE_LOCATION
from models.app_config import ApplicationGroupConfig
from models.application import Application
from models.application_spawner import ApplicationSpawner
from models.workspace import Workspace
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
            global_config = json.load(json_config_file)
            all_workspaces = list(map(lambda w: Workspace(w["name"]), global_config["all_workspaces"])),

            return list(map(lambda config: JSONFileConfigParser.create_from_dict(config, all_workspaces),
                            global_config["group-configs"]))

    @staticmethod
    def create_from_dict(config_dic, all_workspaces):
        return ApplicationGroupConfig(
            name=config_dic["name"],
            all_workspaces=all_workspaces,
            application_spawners=list(map(lambda s:
              ApplicationSpawner(
                  Workspace(s["workspace"]["name"]),
                  Application(s["application"]["execution_path"], s["application"]["window_names"]),
                  s["amount"]
              ),
              config_dic["application_spawners"])
            ),
        )
