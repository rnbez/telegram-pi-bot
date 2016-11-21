#!/usr/bin/python3

# CHANGE YOU <CONTRAB> FILE
# sudo crontab -e
# @reboot python /home/pi/.bot/main.py [TOKEN] [ID] &

import sys
import time
import os
import telepot

import commands
import response_templates as responses

MASTER_ID = os.getenv('TELEGRAM_BOT_MASTER_ID', None)
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', None)
MAX_ERROR_COUNT = 10


def say_hi():
    err_count = 0
    err_msg = ''
    while err_count <= err_count:
        try:
            greetings = responses.greetings(commands.get_ip_addr())
            print(greetings)
            bot.sendMessage(MASTER_ID, greetings, parse_mode='Markdown')
            return
        except:
            err_count += 1
            err_msg = 'Unexpected error: ' + sys.exc_info()[0]
            print(err_msg, '\n\n\n')
    if err_count == err_count:
        raise Exception(err_msg)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    # print(msg)
    # print(content_type, chat_type, chat_id)

    if content_type == 'text':
        answer = commands.handle_commands(msg['text'])
        bot.sendMessage(chat_id, answer, parse_mode='Markdown')

if __name__ == '__main__':
    sleep_time = 20
    if len(sys.argv) > 2:
        TOKEN = sys.argv[1]
        MASTER_ID = sys.argv[2]  

    if len(sys.argv) > 3 and sys.argv[3] == 'no-wait':
        sleep_time = 0
    time.sleep(sleep_time)

    if MASTER_ID and TOKEN:
        bot = telepot.Bot(TOKEN)
        bot.message_loop(handle)
        print('Listening ...')
        say_hi()

        # Keep the program running.
        while 1:
            # pass
            time.sleep(0.1)

    print('exiting...')