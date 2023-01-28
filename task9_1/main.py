import telebot
from telebot import types

bot = telebot.TeleBot("5954559514:AAFArRpHdm6n4T4QcEtFzkvBltjrxGkoSW4")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Напиши имя и фамилию')
    bot.register_next_step_handler(message, sentence)


def sentence(message):
    text = message.text
    surname = text.split()[0]
    name = text.split()[1]
    bot.send_message(message.chat.id, f"Вас зовут: {name}, фамилия: {surname}")


bot.infinity_polling()
