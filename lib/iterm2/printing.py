import base64

ESC = 0x1b
ST = 0x07
OSC = f'{ESC}]'
CSI = f'{ESC}['

def dump(data):
    encodedData = base64.b64encode(data[1].encode('utf-8')).decode('ascii')
    userdata = f']1337;SetUserVar={data[0]}={encodedData}'
    string = "\033" + userdata + "\007"
    print(string, end="")
