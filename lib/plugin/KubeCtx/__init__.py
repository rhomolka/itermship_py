from lib.PluginBase import PluginBase

import subprocess

class KubeCtx(PluginBase):
    '''Show kube context name'''
    def __init__(self):
        self.nameslug = 'kubectx'

    def get_plugin_data(self):
        try:
            cmdout = subprocess.run(["kubectl", "config", "current-context"], 
                                    capture_output=True, text = True)
        except FileNotFoundError:
            return ''
        if cmdout.returncode != 0:
            return ''

        stdoutlines = cmdout.stdout.splitlines(False)
        firstline = stdoutlines.pop(0)

        return f'󱃾 {firstline}'

def get_plugin():
    return KubeCtx()
