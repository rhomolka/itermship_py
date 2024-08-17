from abc import ABC, abstractmethod

class PluginBase(ABC):
    '''Abstract base class for API for plugins'''
    def __init__(self):
        self.nameslug = 'UNIMPLEMENTED'

    @abstractmethod
    # return data to dislay,  Or None.
    def getItermData(self):
        pass

    def getNameSlug(self):
        return self.nameslug

    def getPluginInfo(self):
        return [self.nameslug, self.__doc__]
