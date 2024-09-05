from lib.PluginBase import PluginBase
import platform

class Hostname(PluginBase):
    '''Hostname and OStype'''
    def __init__(self):
        self.nameslug = 'hostname'
        self.hostname = platform.node().split('.')[0] # hostname, not fqdn
        self.uname_s  = platform.system()

    def get_plugin_data(self):
        comp_icon = ''
        match self.uname_s:
            case 'Darwin':
                comp_icon = ''
            case 'Linux':
                comp_icon = '󰌽'

        return f'{self.hostname} {comp_icon}'

def get_plugin():
    return Hostname()
