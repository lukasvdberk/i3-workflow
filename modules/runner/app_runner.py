from default_config import I3_CONFIG_FILE, I3_BACKUP_CONFIG_FILE_LOCATION
from models.app_config import AppConfig
from models.application_spawner import ApplicationSpawner
import os
import shutil


class AppRunner:
    def __init__(self, app_config: AppConfig):
        self.app_config = app_config

    def spawn_work_spaces(self):
        """
        Spawns the provided apps provided in the app config.
        NOTE this will edit your i3wm config file
        :return:
        """
        # TODO add config check

        self._assign_windows()

        for app_spawner in self.app_config.get_application_spawners():
            self._spawn_application(app_spawner)

    def _assign_windows(self):
        """
        Modifies user his i3wm config to spawn windows at certain workspaces
        :return:
        """
        # to start in a clean sate
        self._clear_previous_windows_assigment()
        if os.path.isfile(I3_CONFIG_FILE):
            raise Exception('i3 location file does not exists at location ' + I3_CONFIG_FILE)

        # rules for were windows should spawn
        assigned_window_names_rule = []

        for app_spawner in self.app_config.get_application_spawners():
            for window_name in app_spawner.application.get_window_names():
                assigned_window_names_rule.append(f'assign [class="{window_name}"] 4:1')

        self._backup_original_config()
        with open(I3_CONFIG_FILE, 'a') as i3_config_file:
            i3_config_file.writelines(assigned_window_names_rule)

        self._restart_i3_config()

    def _clear_previous_windows_assigment(self):
        try:
            # saves current config as backup
            shutil.copyfile(I3_BACKUP_CONFIG_FILE_LOCATION, I3_CONFIG_FILE)
        except:
            # no previous configuration was set
            pass

    def _backup_original_config(self):
        try:
            if os.path.isfile(I3_BACKUP_CONFIG_FILE_LOCATION):
                return

            # make an backup of the original config file
            shutil.copyfile(I3_CONFIG_FILE, I3_BACKUP_CONFIG_FILE_LOCATION)
        except:
            # no previous configuration was set
            pass

    def _restart_i3_config(self):
        os.system('i3 reload')
        os.system('i3 restart')

    def _spawn_application(self, app_spawner: ApplicationSpawner):
        os.system(f'sh -c "{app_spawner.application.get_execution_path()}" &')
