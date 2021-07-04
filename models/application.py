class Application:
    def __init__(self, execution_path: str):
        self.execution_path = execution_path

    def set_execution_path(self, execution_path):
        self.execution_path = execution_path

    def get_execution_path(self):
        return self.execution_path
