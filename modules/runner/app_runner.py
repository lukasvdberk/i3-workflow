from default_config import I3_CONFIG_FILE
from models.app_config import AppConfig
from models.application_spawner import ApplicationSpawner
import os

class AppRunner:
    def __init__(self, app_config: AppConfig):
        self.app_config = app_config

    def spawn_work_spaces(self):
        # TODO add config check
        for app_spawner in self.app_config.get_application_spawners():
            self._spawn_application(app_spawner)

    def _assign_windows(self):
        self._clear_previous_windows()
        if os.path.isfile(I3_CONFIG_FILE):
            raise Exception('i3 location file does not exists at location ' + I3_CONFIG_FILE)

        assigned_window_names_rule = []

        for app_spawner in self.app_config.get_application_spawners():
            for window_name in app_spawner.application.get_window_names():
                assigned_window_names_rule.append(f'assign [class="{window_name}"] 4:1')

        with open(I3_CONFIG_FILE, 'a') as i3_config_file:
            i3_config_file.writelines(assigned_window_names_rule)

    def _clear_previous_windows(self):
        pass

    def _spawn_application(self, app_spawner: ApplicationSpawner):
        pass
