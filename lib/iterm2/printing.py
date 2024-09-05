import base64

def dump_iterm_var_data(data):
    encodedData = base64.b64encode(data[1].encode('utf-8')).decode('ascii')
    userdata = f']1337;SetUserVar={data[0]}={encodedData}'
    string = "\033" + userdata + "\007"
    print(string, end="")
