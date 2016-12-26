#!/usr/bin/python3

# CHANGE YOU <CONTRAB> FILE
# sudo crontab -e
# @reboot python /home/pi/.bot/main.py [TOKEN] [ID] &

import sys
import time
import os
import telepot

from head import Head

_MASTER_ID_ = os.getenv('TELEGRAM_BOT_MASTER_ID', None)
_TOKEN_ = os.getenv('TELEGRAM_BOT_TOKEN', None)
_HEAD_ = None


def say_hi():
    err_count = 0
    err_msg = ''
    while err_count <= err_count:
        try:            
            greetings = _HEAD_.greetings()
            print(greetings)
            bot.sendMessage(_MASTER_ID_, greetings, parse_mode='Markdown')
            return
        except:
            err_count += 1
            err_msg = 'Unexpected error: ' + sys.exc_info()[0]
            print(err_msg, '\n\n\n')
    if err_count == err_count:
        raise Exception(err_msg)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if content_type == 'text':
        answer = _HEAD_.handle_commands(msg['text'])
        bot.sendMessage(chat_id, answer, parse_mode='Markdown')

if __name__ == '__main__':
    sleep_time = 20
    if len(sys.argv) > 2:
        _TOKEN_ = sys.argv[1]
        _MASTER_ID_ = sys.argv[2]  

    if len(sys.argv) > 3 and sys.argv[3] == 'no-wait':
        sleep_time = 0
    time.sleep(sleep_time)

    if _MASTER_ID_ and _TOKEN_:
        bot = None        
        while True:            
            try:                
                bot = telepot.Bot(_TOKEN_)    
                _HEAD_ = Head(bot)
                bot.message_loop(handle)
                print('Listening ...')
                say_hi()
                break
            except:
                print("error... retrying in {0} seconds".format(sleep_time))
                time.sleep(sleep_time)

        # Keep the program running.
        while True:
            pass

    print('exiting...')