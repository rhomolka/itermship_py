#!/usr/bin/env python3

import lib.iterm2.printing as printing
# lib.plugin imports recursively
from lib.PluginBase import PluginBase
# iterates and gets all the plugin
import lib.plugin
import sys, os, argparse

def parse_app_args():
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

def get_plugin_list():
    '''Get a list of plugin classes from plugin code dir'''
    pluginnames = [ name for name in sys.modules.keys() 
                   if 'lib.plugin.' in name ]
    module_list = [ sys.modules[name] for name in pluginnames ]
    # modulelist will have all modules in lib.plugin....
    # but only the base __init__ module will have the getPlugin() function
    plugin_list = [ module.get_plugin() for module in module_list \
        if '/__init__.py' in module.__file__ ]
    plugin_list = [ x for x in plugin_list if issubclass(x.__class__, PluginBase) ]
    return(plugin_list)

def dump_all_plugin_info():
    '''Dump docstrings for all plugins'''
    plugin_list = get_plugin_list()
    
    for plugin in plugin_list:
        nameslug = plugin.get_nameslug()
        doc = plugin.__class__.__doc__
        
        print(f'{nameslug}: {doc}')

def dump_all_plugin_data():
    '''Dump data for all plugins'''
    plugin_list = get_plugin_list()
    
    for plugin in plugin_list:
        nameslug = plugin.get_nameslug()
        plugin_data = plugin.get_plugin_data()
        if plugin_data is None: plugin_data = ''
        print(f'{nameslug}: {plugin_data}')

def dump_plugin_data_term_vars():
    '''Dump the plugin output to Iterm Var format
    
       Possibly filtered by ITERMSHIPPLUGINS content
    '''
    data_array = []
    plugin_list = get_plugin_list()

    for plugin in plugin_list:
        nameslug = plugin.get_nameslug()
        ENV_ITERMSHIPPLUGINS = os.environ.get('ITERMSHIPPLUGINS')
        if ENV_ITERMSHIPPLUGINS is not None and \
                f'|{nameslug}|' not in ENV_ITERMSHIPPLUGINS:
            # no data for this, wipe out any existing data with blanks
            data_array.append([nameslug, ''])
        else:
            pluginData = plugin.get_plugin_data()
            if pluginData is not None:
                data_array.append([nameslug, pluginData])
            else:
                data_array.append([nameslug, ''])

    for data in data_array:
        printing.dump_iterm_var_data(data)
    
def main():
    args = parse_app_args()
    
    if args['plugin_info']:
        dump_all_plugin_info()
    elif args['print_data']:
        dump_all_plugin_data()
    else:
        dump_plugin_data_term_vars()

if __name__ == '__main__':
    main()