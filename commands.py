import subprocess
import response_templates as responses


def get_ip_addr():
    addr = subprocess.getoutput('hostname -I')
    return addr.split(maxsplit=1)[0]

def get_command_and_params(msg):
    v = msg.replace('/', '', 1).lower().split(maxsplit=1)
    if len(v) > 1:
        return v
    
    return v[0], None


def handle_commands(msg):
    cmd, params = get_command_and_params(msg)
    print(cmd, params)
    if cmd == 'hello' or cmd == 'hi' or cmd == 'what\'s up' or cmd == 'help':
        return responses.help()  

    if cmd == 'ip':
        return responses.myip(get_ip_addr())

    return responses.sorry()
