from abc import ABC, abstractmethod

class PluginBase(ABC):
    '''Abstract base class for API for plugins'''
    def __init__(self):
        self.nameslug = 'UNIMPLEMENTED'

    @abstractmethod
    # return data to dislay,  Or None.
    def get_plugin_data(self):
        pass

    def get_nameslug(self):
        return self.nameslug

    def get_plugin_info(self):
        return [self.nameslug, self.__doc__]
