
def greetings(ip):
    m = "Hi, I'm up!\nMy IP Address is *{0}*.".format(ip)
    return m

def myip(ip):
    return "My current local IP Address is {0}.".format(ip)

def sorry():
    return "Sorry, I don't understand what you mean."

def repeat(msg):
    return "You said: " + msg

_help_ = '''Hi, I'm _EvvaPi Bot_.

```text
You can say [hello], [hi], [what's up?], [start] or [help] to see the list of commands I know.
------------------
    ip: returns my current local IP address.
    run [command]: runs a given command and returns its output.

```
'''
def help():
    return _help_

def command_output(output):
    return "```text ### Command Output ### \n\n{0}\n\n ### Output End ###```".format(output)