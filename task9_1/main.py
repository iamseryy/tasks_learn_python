import telebot
from telebot import types

bot = telebot.TeleBot("5954559514:AAFArRpHdm6n4T4QcEtFzkvBltjrxGkoSW4")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, message)


bot.infinity_polling()
