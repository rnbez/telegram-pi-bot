
def greetings(ip):
    m = "Hi, I'm up!\nMy IP Address is {0}.".format(ip)
    return m

def myip(ip):
    return "My current local IP Address is {0}.".format(ip)

def sorry():
    return "Sorry, I don't understand what you mean."

_help_ = '''Hi, I'm EvvaPi Bot.
You can say "hello", "hi", "what's up?" or 'help' to see the list of commands I know.
------------------
    ip: returns my current local IP address.
'''
def help():
    return _help_