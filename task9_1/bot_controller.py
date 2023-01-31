import telebot
from telebot import types
import service
import properties
import logging


bot = telebot.TeleBot(properties.BOT_TOKEN)
user_message = ''
is_game_started = False


def start():
    logging.info(f" : start bot")
    bot.infinity_polling()


@bot.message_handler(commands=['start'])
def button(message):
    logging.info(f" : user id {message.chat.id} : username {message.chat.username} : "
                 f"command {message.html_text}")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but_rules = types.KeyboardButton("Правила")
    but_play_bot = types.KeyboardButton("Играть с обычным ботом")
    but_play_smart_bot = types.KeyboardButton("Играть с умным ботом")
    but_game_stop = types.KeyboardButton("Остановить игру")
    markup.add(but_rules)
    markup.add(but_play_bot)
    markup.add(but_play_smart_bot)
    markup.add(but_game_stop)
    bot.send_message(message.chat.id, "Ваш выбор, меню ниже", reply_markup=markup)


@bot.message_handler(content_types="text")
def controller(message):
    global is_game_started
    global user_message

    logging.info(f" : user id {message.chat.id} : username {message.chat.username} : "
                 f"text_message '{message.text}' ")

    if message.text == "Правила":
        bot.send_message(message.chat.id, service.get_rules())
        if is_game_started:
            check_user_message(message)
        else:
            button(message)

    elif message.text == "Играть с обычным ботом":
        play(service.get_bot_player(), message)

    elif message.text == "Играть с умным ботом":
        play(service.get_smart_bot_player(), message)

    elif message.text == "Остановить игру":
        if not is_game_started:
            bot.send_message(message.chat.id, "Игра еще не запущена")
        else:
            is_game_started = False
            user_message = ''
            bot.send_message(message.chat.id, "Игра остановлена")
        button(message)

    elif is_game_started:
        check_user_message(message)

    else:
        bot.send_message(message.chat.id, "Ваш выбор, меню ниже")


def play(player, message):
    global is_game_started
    global user_message

    if is_game_started:
        bot.send_message(message.chat.id, "Игра уже запущена")
        bot.send_message(message.chat.id, "Ваш ход")
        return
    else:
        is_game_started = True
        players = service.get_players(service.get_human_player(str(message.chat.first_name)), player)
        winner = service.process(players, properties.NUMBER_CANDIES, properties.MAX_CANDIES_FOR_TURN, message)
        if winner:
            bot.send_message(message.chat.id, f"Победитель - {winner}")
            bot.send_message(message.chat.id, "Игра закончена")
            button(message)
        is_game_started = False


def check_user_message(message):
    global user_message

    if message.text.isdigit():
        num = int(message.text)
        if 0 < num <= properties.MAX_CANDIES_FOR_TURN:
            user_message = message.text
        else:
            bot.send_message(message.chat.id,
                             f"Вы можете взять от 1 до {properties.MAX_CANDIES_FOR_TURN} конфет! Попробуйте снова")
            user_message = ''
    else:
        if message.text == "Правила":
            bot.send_message(message.chat.id, "Ваш ход")
        else:
            bot.send_message(message.chat.id, "Неправильно! Попробуйте снова")


def send_message(message, mess):
    bot.send_message(message.chat.id, mess)
