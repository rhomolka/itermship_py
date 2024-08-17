from lib.PluginBase import PluginBase
import platform

class Hostname(PluginBase):
    '''Hostname and OStype'''
    def __init__(self):
        self.nameslug = 'hostname'
        self.hostname = platform.node().split('.')[0] # hostname, not fqdn
        self.uname_s  = platform.system()

    def getItermData(self):
        compIcon = ''
        match self.uname_s:
            case 'Darwin':
                compIcon = ''
            case 'Linux':
                compIcon = '󰌽'

        return f'{self.hostname} {compIcon}'

def getPlugin():
    return Hostname()
