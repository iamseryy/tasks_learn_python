from random import shuffle, randint
import bot_controller as bot
import properties


def get_rules():
    return f'На столе лежит {properties.NUMBER_CANDIES} конфета. Играют два игрока делая ход друг после друга. ' \
            f'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем ' \
            f'{properties.MAX_CANDIES_FOR_TURN} конфет. Все конфеты оппонента достаются сделавшему последний ход.'


def get_players(player1, player2):
    players = [player1, player2]
    shuffle(players)
    return players


def get_human_player(name):
    return name, human_turn


def get_bot_player():
    return "bot", bot_turn


def get_smart_bot_player():
    return "smart bot", smart_bot_turn


def human_turn(human, remainder, max_amount, message):
    user_message = ''
    bot.user_message = ''
    bot.send_message(message, f"Ваша очередь {human}:")
    while bot.is_game_started and not user_message.isdigit():
        user_message = bot.user_message
    if user_message.isdigit():
        return int(user_message)
    else:
        return False


def bot_turn(creature, remainder, max_amount, message):
    num = randint(1, max_amount)
    bot.send_message(message, f"{creature} взял {num} конфет")
    return num


def smart_bot_turn(creature, remainder, max_amount, message):
    num = remainder % (max_amount + 1)
    if num == 0:
        num = max_amount
    bot.send_message(message, f"{creature} взял {num} конфет")
    return num


def process(players, number, max_amount, message):
    bot.send_message(message, "Игра началась")
    while True:
        for player in players:
            bot.send_message(message, f"Конфет на столе: {number}")
            turn_number = player[1](player[0], number, max_amount, message)
            if type(turn_number) is bool and not turn_number:
                return False
            number -= turn_number
            if number <= max_amount:
                bot.send_message(message, f"Конфет на столе: {number}")
                players.remove(player)
                return players[0][0]