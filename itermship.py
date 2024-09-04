#!/usr/bin/env python3

import lib.iterm2.printing as printing
# lib.plugin imports recursively
from lib.PluginBase import PluginBase
# iterates and gets all the plugin
import lib.plugin
import sys, os, argparse

def parseAppArgs():
    parser = argparse.ArgumentParser(prog='itermship',
                                     description='Give useful info to iterm',
                                     epilog='ENV Var ITERMSHIPPLUGINS can be used to filter plugins')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--plugin-info', action='store_true', help='Dump info on what plugins do')
    group.add_argument('--print-data',  action='store_true', help='Print data for all plugins to terminal')
    optdata = parser.parse_args()
    retval = {}
    retval['plugin_info'] = optdata.plugin_info
    retval['print_data']  = optdata.print_data
    
    return retval

def getPluginList():
    '''Get a list of plugin classes from plugin code dir'''
    pluginnames = [ name for name in sys.modules.keys() 
                   if 'lib.plugin.' in name ]
    moduleList = [ sys.modules[name] for name in pluginnames ]
    # modulelist will have all modules in lib.plugin....
    # but only the base __init__ module will have the getPlugin() function
    pluginList = [ module.getPlugin() for module in moduleList \
        if '/__init__.py' in module.__file__ ]
    pluginList = [ x for x in pluginList if issubclass(x.__class__, PluginBase) ]
    return(pluginList)

def dumpAllPluginInfo():
    '''Dump docstrings for all plugins'''
    pluginList = getPluginList()
    
    for plugin in pluginList:
        nameslug = plugin.getNameSlug()
        doc = plugin.__class__.__doc__
        
        print(f'{nameslug}: {doc}')

def dumpAllPluginData():
    '''Dump data for all plugins'''
    pluginList = getPluginList()
    
    for plugin in pluginList:
        nameslug = plugin.getNameSlug()
        pluginData = plugin.getItermData()
        if pluginData is None: pluginData = ''
        print(f'{nameslug}: {pluginData}')

def dumpPluginDataToIterm():
    '''Dump the plugin output to Iterm Var format'''
    dataArray = []
    pluginList = getPluginList()

    for plugin in pluginList:
        nameslug = plugin.getNameSlug()
        ENV_ITERMSHIPPLUGINS = os.environ.get('ITERMSHIPPLUGINS')
        if ENV_ITERMSHIPPLUGINS is not None and \
                f'|{nameslug}|' not in ENV_ITERMSHIPPLUGINS:
            # no data for this, wipe out any existing data with blanks
            dataArray.append([nameslug, ''])
        else:
            pluginData = plugin.getItermData()
            if pluginData is not None:
                dataArray.append([nameslug, pluginData])
            else:
                dataArray.append([nameslug, ''])

    for data in dataArray:
        printing.dumpAsItermData(data)
    
def main():
    args = parseAppArgs()
    
    if args['plugin_info']:
        dumpAllPluginInfo()
    elif args['print_data']:
        dumpAllPluginData()
    else:
        dumpPluginDataToIterm()

if __name__ == '__main__':
    main()