import subprocess
import response_templates as responses

def run_command(command):
    return subprocess.getoutput(command)

def get_ip_addr():
    # addr = subprocess.getoutput('hostname -I')
    addr = run_command('hostname -I')
    return addr.split(maxsplit=1)[0]

def get_command_and_params(msg):
    v = msg.replace('/', '', 1).split(maxsplit=1)
    if len(v) > 1:
        return v[0].lower(), v[1]
    
    return v[0].lower(), None


def handle_commands(msg):
    cmd, params = get_command_and_params(msg)
    print(cmd, params)
    if cmd == 'start' or cmd == 'hello' or cmd == 'hi' or cmd == 'what\'s up' or cmd == 'help':
        return responses.help()  

    if cmd == 'run':
        return responses.command_output(run_command(params))

    if cmd == 'ip':
        return responses.myip(get_ip_addr())
    
    if cmd == 'repeat':
        return responses.repeat(params)

    return responses.sorry()
