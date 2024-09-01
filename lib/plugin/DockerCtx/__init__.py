from lib.PluginBase import PluginBase

import subprocess

class DockerCtx(PluginBase):
    '''Show docker context'''
    def __init__(self):
        self.nameslug = 'dockerctx'

    def getItermData(self):
        try:
            cmdout = subprocess.run(["docker", "context", "show"], 
                                    capture_output=True, text = True)
        except FileNotFoundError:
            return ''
        if cmdout.returncode != 0:
            return ''

        stdoutlines = cmdout.stdout.splitlines(False)
        firstline = stdoutlines.pop(0)

        return f' {firstline}'

def getPlugin():
    return DockerCtx()
