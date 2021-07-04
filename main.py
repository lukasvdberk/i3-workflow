from models.app_config import ApplicationConfig
from models.application import Application
from models.application_spawner import ApplicationSpawner
from models.workspace import Workspace
from modules.configs.config_factory import ConfigFactory
from modules.runner.app_runner import ApplicationRunner


def main_json_config():
    app = ConfigFactory.get_default_parser().get_config()
    print(app)
    # app.spawn_work_spaces()


def main_python_config():
    app_spawners = [
        ApplicationSpawner(Workspace("5:2"), Application("/usr/bin/firefox", ["Firefox", "firefox"]), 4),
        ApplicationSpawner(Workspace("5:2"), Application("/Applications/Shadow.AppImage --no-sandbox", ["Shadow", "shadow"]), 1),
        ApplicationSpawner(Workspace("6:2"), Application("/usr/bin/kitty", ["kitty", "Kitty"]), 4),
    ]
    # not used yet
    all_workspaces = []
    app_config = ApplicationConfig(app_spawners, all_workspaces)

    app = ApplicationRunner(app_config)
    app.spawn_work_spaces()


if __name__ == '__main__':
    main_json_config()
