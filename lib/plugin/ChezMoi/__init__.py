from lib.PluginBase import PluginBase

import os

class Chezmoi(PluginBase):
    '''Indicate whether you're in a ChezMoi context'''
    def __init__(self):
        self.nameslug = 'chezmoi'

    def getItermData(self):
        if 'CHEZMOI' in os.environ:
            return '🇫🇷'
        else:
            return ''

def getPlugin():
    return Chezmoi()
