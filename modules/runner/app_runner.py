from models.app_config import AppConfig
from models.application_spawner import ApplicationSpawner


class AppRunner:
    def __init__(self, app_config: AppConfig):
        self.app_config = app_config

    def spawn_work_spaces(self):
        # TODO add config check
        for app_spawner in self.app_config.get_application_spawners():
            self._spawn_application(app_spawner)

    def _assign_windows(self):
        pass

    def _spawn_application(self, app_spawner: ApplicationSpawner):
        pass
