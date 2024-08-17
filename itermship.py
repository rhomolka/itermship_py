#!/usr/bin/env python3

import lib.iterm2.printing as printing
# lib.plugin imports recursively
from lib.PluginBase import PluginBase
# iterates and gets all the plugin
import lib.plugin
import sys, os

dataArray = []

def getPluginList():
    pluginnames = [ name for name in sys.modules.keys() 
                   if 'lib.plugin.' in name ]
    pluginList = [ sys.modules[name].getPlugin() for name in pluginnames ]
    pluginList = [ x for x in pluginList if issubclass(x.__class__, PluginBase) ]
    return(pluginList)

def main():
    pluginList = getPluginList()

    for plugin in pluginList:
        nameslug = plugin.getNameSlug()
        ENV_ITERSHIPPLUGINS = os.environ.get('ITERMSHIPPLUGINS')
        if ENV_ITERSHIPPLUGINS is not None and \
                f'|{nameslug}|' not in ENV_ITERSHIPPLUGINS:
            dataArray.append([nameslug, ''])
        else:
            pluginData = plugin.getItermData()
            if pluginData is not None:
                dataArray.append([nameslug, pluginData])
            else:
                dataArray.append([nameslug, ''])

    for data in dataArray:
        printing.dump(data)
        
if __name__ == '__main__':
    main()