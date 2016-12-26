class Mouth():

    def __init__(self, bot = None):
        if bot:
            me = bot.getMe()
            self.bot_username = me['username']
            self.bot_name = me['first_name']
            self.bot_id = me['id']
    
    def greetings(self, ip):
        m = "Hi, I'm up!\nMy IP Address is *{0}*.".format(ip)
        return m

    def myip(self, ip):
        return "My current local IP Address is {0}.".format(ip)

    def sorry(self):
        return "Sorry, I don't understand what you mean."

    def help(self):   
        _help_ = ''
        _help_ += "Hi, I'm _{0}_.".format(self.bot_name)

        _help_ += "```text"
        _help_ += "You can say [hello], [hi], [what's up?], [start] or [help] to see the list of commands I know."
        _help_ += "------------------"
        _help_ += "    ip: returns my current local IP address."
        _help_ += "    vnc: launches vncserver at port 1."
        _help_ += "    run [command]: runs a given command and returns its output."
        _help_ += "```"
        return _help_

    def command_output(self, output):
        return "```text ### Command Output ### \n\n{0}\n\n ### Output End ###```".format(output)