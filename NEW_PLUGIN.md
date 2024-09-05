1. Make a new directory in lib/plugin, e.g. NewPlugin
1. Make a `NewPlugin/__init__.py` module in the new directory.  Module should:
    1. `from lib.PluginBase import PluginBase`
    1. Declare a class that inherits from PluginBase
1. Class should:
    1. Have a doc_string
    1. Set member `self.nameslug` to a string.  this needs to be unique among modules.  Nameslug will be used for the user variable for iterm2, and also module filtering in env `ITERMSHIPPLUGINS`
    1. Have a member function get_plugin_data() which passes the data to iterm2
1. Module should also:
	1. Have a function get_plugin() which returns an instance of the class.

The supplied Hostname and ChezMoi are pretty simple plugins and can be used as examples.  