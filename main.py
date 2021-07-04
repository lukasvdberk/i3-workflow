from models.app_config import ApplicationConfig
from modules.configs.config_factory import ConfigFactory
from modules.runner.app_runner import ApplicationRunner
from pick import pick


def pick_config(app_configs: list[ApplicationConfig]):
    title = 'Choose which app config to start:  '
    config_options = list(map(lambda c: c.get_config_name(), app_configs))
    option, index = pick(config_options, title)

    return app_configs[index]


def main():
    app_configs = ConfigFactory.get_default_parser().get_config()

    chosen_app_config = pick_config(app_configs)
    app_runner = ApplicationRunner(chosen_app_config)
    app_runner.spawn_work_spaces()


if __name__ == '__main__':
    main()
