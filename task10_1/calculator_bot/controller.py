import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup

import service
import properties
import logging


markup: ReplyKeyboardMarkup

bot = telebot.TeleBot(properties.BOT_TOKEN)

first_num = ""
second_num = ""


def start():
    logging.info("Start bot")
    bot.infinity_polling()


@bot.message_handler(commands=['start'])
def button(message):
    global markup
    global first_num
    global second_num

    first_num = ""
    second_num = ""

    bot.send_message(message.chat.id, "Hi! This is a calculator for real numbers and complex numbers. "
                                      "Complex numbers can be entered in the format a + bi or a + bj "
                                      "and don't worry about spaces. "
                                      "First enter two numbers in order, then select an operation")

    logging.info(f" : user id {message.from_user.id} : user full_name {message.from_user.full_name} : "
                 f"text_message '{message.text}' ")

    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    but_plus = types.KeyboardButton("+")
    but_minus = types.KeyboardButton("-")
    but_mult = types.KeyboardButton("*")
    but_div = types.KeyboardButton("/")
    but_div_int = types.KeyboardButton("//")
    but_div_remainder = types.KeyboardButton("%")
    but_cancel = types.KeyboardButton("Cancel")
    markup.add(but_plus, but_minus)
    markup.add(but_mult, but_div)
    markup.add(but_div_int, but_div_remainder)
    markup.add(but_cancel)
    bot.send_message(message.chat.id, "Enter the first number")


@bot.message_handler(content_types="text")
def controller(message):
    global markup
    global first_num
    global second_num

    logging.info(f" : user id {message.from_user.id} : user full_name {message.from_user.full_name} : "
                 f"text_message '{message.text}' ")

    if message.text == "Cancel":
        bot.send_message(message.chat.id, "Canceled\nEnter the first number")
        first_num = ""
        second_num = ""

    elif message.text == "+":
        calculate(lambda x, y: x + y, message)

    elif message.text == "-":
        calculate(lambda x, y: x - y, message)

    elif message.text == "*":
        calculate(lambda x, y: x * y, message)

    elif message.text == "/":
        try:
            calculate(lambda x, y: x / y, message)
        except ZeroDivisionError:
            first_num = ""
            second_num = ""
            bot.send_message(message.chat.id, "Error, division by zero\nEnter the first number")

    elif message.text == "//":
        try:
            calculate(lambda x, y: x // y, message)
        except TypeError:
            first_num = ""
            second_num = ""
            bot.send_message(message.chat.id, "Error, unsupported operation\nEnter the first number")
        except ZeroDivisionError:
            first_num = ""
            second_num = ""
            bot.send_message(message.chat.id, "Error, division by zero\nEnter the first number")

    elif message.text == "%":
        try:
            calculate(lambda x, y: x % y, message)
        except TypeError:
            first_num = ""
            second_num = ""
            bot.send_message(message.chat.id, "Error, unsupported operation\nEnter the first number")
        except ZeroDivisionError:
            first_num = ""
            second_num = ""
            bot.send_message(message.chat.id, "Error, division by zero\nEnter the first number")

    else:
        number = service.get_number(message.text.replace(' ', '').replace('i', 'j'))
        if type(number) is bool and not number:
            if not first_num:
                bot.send_message(message.chat.id, "Invalid! Try Again\nEnter the first number")
            else:
                bot.send_message(message.chat.id, "Invalid! Try Again\nEnter the second number")
        else:
            if first_num == '':
                first_num = number
                bot.send_message(message.chat.id, "Enter the second number")
            else:
                second_num = number
                bot.send_message(message.chat.id, "Choose an operation below", reply_markup=markup)


def calculate(operation, message):
    global first_num
    global second_num

    if first_num != '' and second_num != '':
        res = service.calculate(first_num, second_num, operation)
        bot.send_message(message.chat.id, f"Result = {str(res).replace('j', 'i')}")
        first_num = ''
        second_num = ''
        bot.send_message(message.chat.id, "Enter the first number")
    else:
        bot.send_message(message.chat.id, "Numbers must be entered first")
        if not first_num:
            bot.send_message(message.chat.id, "Enter the first number")
        elif not second_num:
            bot.send_message(message.chat.id, "Enter the second number")