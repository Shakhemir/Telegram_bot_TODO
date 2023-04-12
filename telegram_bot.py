import time

import telebot
from config import menu
import controller as c
# import schedule
# import threading
import os

is_polling = True


def telegram_bot():
    bot = telebot.TeleBot(os.getenv('TOKEN'))
    print('Time is', time.strftime("%H:%M:%S", time.localtime()))
    # print('Stop time is', STOP_TIME)

    def bot_polling():
        while is_polling:
            try:
                bot.polling()
            except Exception as ex:
                print('Exception:', ex)

    def stop_polling():
        global is_polling
        print('Stop polling')
        bot.stop_polling()
        is_polling = False

    @bot.message_handler(commands=menu)
    def commands(message):
        handler(c.command_handler, message)

    @bot.message_handler(content_types=['text'])
    def commands(message):
        handler(c.message_handler, message)

    def handler(function, message):
        chat_id = message.chat.id
        txt = message.text
        answer = function(message, txt)
        if answer:
            if answer == 'stop':
                stop_polling()
            send_message(chat_id, answer)

    def send_message(chat_id, txt):
        bot.send_message(chat_id, txt, parse_mode='Markdown')

    bot_polling()
