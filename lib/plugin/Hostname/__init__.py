import platform
def getItermData():
    hostname = platform.node().split('.')[0]
    uname_s = platform.system()

    compIcon = ''
    match uname_s:
        case 'Darwin':
            compIcon = ''
        case 'Linux':
            compIcon = '󰌽'
            
    return ['hostname', f'{hostname} {compIcon}']
