# combines application and the workspace it should be deployed to
from models.application import Application
from models.workspace import Workspace


class ApplicationSpawner:
    def __init__(self, workspace: Workspace, application: Application):
        """
        Application spawner combines the workspace and application to be spawned
        :param workspace: On which workspace it should spawn
        :param application: The application to spawn on the defined workspace
        """
        self.workspace = workspace
        self.application = application
        self.amount = 1

    def __init__(self, workspace: Workspace, application: Application, amount: int):
        """
        Application spawner combines the workspace and application to be spawned
        :param workspace: On which workspace it should spawn
        :param application: The application to spawn on the defined workspace
        :param amount: Amount of time the application should spawn on the given workspace
        """
        self.workspace = workspace
        self.application = application
        self.amount = amount

    def set_workspace(self, workspace: Workspace):
        self.workspace = workspace

    def get_workspace(self):
        return self.workspace

    def set_application(self, application: Application):
        self.application = application

    def get_application(self):
        return self.application

    def set_amount_of_applications_to_spawn(self, amount: int):
        self.amount = amount

    def get_amount_of_applications_to_spawn(self):
        return self.amount