'''dynamically pick up plugins in lib/plugin/*/__init__.py form'''

import os, inspect

 # realpath() will make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))

# dynamically pick up plugins
for item in os.listdir(cmd_folder):
    if item == '__init__.py' or not os.path.isfile(f"{cmd_folder}/{item}/__init__.py"):
        continue
    __import__(f"lib.plugin.{item}", locals(), globals())
