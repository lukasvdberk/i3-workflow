from models.app_config import ApplicationGroupConfig


class AppConfigChecker:
    def __init__(self, app_config: ApplicationGroupConfig):
        self.app_config = app_config

    def do_all_workspaces_exist_of_config(self):
        """
        Determines if all workspaces currently defined in the config actually also exists in i3
        :return: A boolean if all workspaces exists
        """
        # TODO implement
        pass

    def check_all(self):
        """
        Checks all the configuration
        :return: A boolean whether all the checks have passed
        """
        # TODO implement
        pass