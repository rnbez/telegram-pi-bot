import subprocess
from mouth import Mouth

class Head():
    def __init__(self, bot):
        if bot:
            self.mouth = Mouth(bot)

    def run_command(self, command):
        return subprocess.getoutput(command)

    def get_ip_addr(self):
        # addr = subprocess.getoutput('hostname -I')
        addr = self.run_command('hostname -I')
        return addr.split(maxsplit=1)[0]

    def start_vncserver(self):
        return self.run_command('vncserver :1')

    def get_command_and_params(self, msg):
        v = msg.replace('/', '', 1).split(maxsplit=1)
        if len(v) > 1:
            return v[0].lower(), v[1]
        
        return v[0].lower(), None


    def handle_commands(self, msg):
        cmd, params = self.get_command_and_params(msg)
        print(cmd, params)
        if cmd == 'start' or cmd == 'hello' or cmd == 'hi' or cmd == 'what\'s up' or cmd == 'help':
            return self.mouth.help()

        if cmd == 'run':
            return self.mouth.command_output(self.run_command(params))

        if cmd == 'ip':
            return self.mouth.myip(self.get_ip_addr())

        if cmd == 'vnc':
            return self.mouth.command_output(self.start_vncserver())
        
        return self.mouth.sorry()

    def greetings(self):
        return self.mouth.greetings(self.get_ip_addr())