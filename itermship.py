#!/usr/bin/env python3

import lib.iterm2.printing as printing
# lib.plugin imports recursively
import lib.plugin
import sys

dataArray = []

def main():
    pluginnames = [ name for name in sys.modules.keys() 
                   if 'lib.plugin.' in name ]
    for name in pluginnames:
        pluginData = sys.modules[name].getItermData()
        if pluginData is not None:
            dataArray.append(pluginData)
    for data in dataArray:
        printing.dump(data)
        
if __name__ == '__main__':
    main()