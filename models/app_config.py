from models.application_spawner import ApplicationSpawner
from models.workspace import Workspace


class ApplicationConfig:
    def __init__(self, application_spawners: list[ApplicationSpawner], all_workspaces: list[Workspace]):
        self.application_spawners = application_spawners
        self.all_workspaces = all_workspaces

    def get_application_spawners(self):
        return self.application_spawners

    def get_all_workspaces(self):
        return self.all_workspaces
