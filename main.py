from models.app_config import ApplicationGroupConfig
from modules.configs.config_factory import ConfigFactory
from modules.runner.app_runner import ApplicationRunner
from pick import pick


def pick_config(app_configs: list[ApplicationGroupConfig]):
    title = 'Choose which workflow config to start:  '
    config_options = list(map(lambda c: c.get_config_name(), app_configs))
    option, index = pick(config_options, title, indicator='=> ')

    return app_configs[index]


def main():
    group_configs = ConfigFactory.get_default_parser().get_config()

    chosen_group_config = pick_config(group_configs)
    app_runner = ApplicationRunner(chosen_group_config)
    app_runner.spawn_work_spaces()

    input("Press enter to confirm all the windows have started (you config will be restored)")
    app_runner.restore_config()


if __name__ == '__main__':
    main()
