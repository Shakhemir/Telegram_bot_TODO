from Token import TOKEN
import telebot
from config import menu
import controller as c


def telegram_bot():
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=menu)
    def commands(message):
        handler(c.command_handler, message)

    @bot.message_handler(content_types='text')
    def commands(message):
        handler(c.message_handler, message)

    def handler(function, message):
        chat_id = message.chat.id
        txt = message.text
        answer = function(chat_id, txt)
        if answer:
            send_message(chat_id, answer)

    def send_message(chat_id, txt):
        bot.send_message(chat_id, txt, parse_mode='Markdown')

    bot.polling()
