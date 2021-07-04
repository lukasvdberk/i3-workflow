class Application:
    def __init__(self, execution_path: str, window_names: list[str]):
        self.execution_path = execution_path
        self.window_names = window_names

    def set_execution_path(self, execution_path):
        self.execution_path = execution_path

    def get_execution_path(self):
        return self.execution_path

    def get_window_names(self):
        return self.window_names
