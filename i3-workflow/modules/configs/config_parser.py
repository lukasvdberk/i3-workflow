import abc


class IConfigParser:
    @abc.abstractmethod
    def get_config(self):
        raise NotImplemented("No implementation given for get_config method.")
