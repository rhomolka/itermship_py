import os
def getItermData():
    if 'CHEZMOI' in os.environ:
        return ['chezmoi','🇫🇷']
    else:
        return ['chezmoi','']