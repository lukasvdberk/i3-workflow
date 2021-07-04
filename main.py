from models.app_config import ApplicationConfig
from models.application import Application
from models.application_spawner import ApplicationSpawner
from models.workspace import Workspace
from modules.runner.app_runner import ApplicationRunner


def main():
    app_spawners = [
        ApplicationSpawner(Workspace("5:2"), Application("/usr/bin/firefox", ["Firefox", "firefox"]), 1)
    ]
    # not used yet
    all_workspaces = []
    app_config = ApplicationConfig(app_spawners, all_workspaces)

    app = ApplicationRunner(app_config)
    app.spawn_work_spaces()


if __name__ == '__main__':
    main()
