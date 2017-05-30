import time
import random
import datetime
import telepot
import sys
from telepot.loop import MessageLoop

"""
Starting my bot in python! AI.

"""

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/start':
        bot.sendMessage(chat_id, str("Welcome to Raspberry Pi!") )
    elif command == 'Hello':
        bot.sendMessage(chat_id, str("Hi"))
    elif command == '/temperature':
        bot.sendMessage(chat_id, "The temperature of the Raspberry Pi is " + str( int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3) + " degree celcius.")
    

bot = telepot.Bot('386863341:AAEstGzCzO0ilJ7XMTYMt24DDGpgg0aOU-I')

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)
