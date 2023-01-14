# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""

from random import shuffle, randint


def get_players(player1, player2):
    players = [player1, player2]
    shuffle(players)
    return players


def get_human_player(num):
    return input(f"\nEnter player name {num}: "), human_turn


def get_bot_player():
    return "bot", bot_turn


def get_smart_bot_player():
    return "smart bot", smart_bot_turn


def human_turn(human, remainder, max_amount):
    line = ""
    while not line.isdigit():
        line = input(f"Your turn {human}: ")
        if line.isdigit():
            num = int(line)
            if 0 < num <= max_amount:
                return num
            else:
                print(f"You can take at least 1 and no more than {max_amount} candies! Try Again\n")
                line = ""
                continue
        print("Invalid! Try Again\n")


def bot_turn(creature, remainder, max_amount):
    num = randint(1, max_amount)
    print(f"{creature} took {num} candies")
    return num


def smart_bot_turn(creature, remainder, max_amount):
    num = remainder % (max_amount + 1)
    if num == 0:
        num = max_amount
    print(f"{creature} took {num} candies")
    return num


def process(players, number, max_amount):
    print("\nThe game started")
    while True:
        for player in players:
            print(f"\nCandies on the table: {number} ")
            number -= player[1](player[0], number, max_amount)
            if number <= max_amount:
                print(f"\nCandies on the table: {number} ")
                players.remove(player)
                return players[0][0]


def game(number_candies, max_candies):
    while True:
        print("\nCandy game\n")
        print("Press 1 to play with a man")
        print("Press 2 to play with a bot")
        print("Press 3 to play with a smart bot")
        print("Press 4 to Quit\n")
        item = input("Your choice: ")
        if item == '1':
            win = process(get_players(get_human_player(1), get_human_player(2)), number_candies, max_candies)
        elif item == '2':
            win = process(get_players(get_human_player(''), get_bot_player()), number_candies, max_candies)
        elif item == '3':
            win = process(get_players(get_human_player(''), get_smart_bot_player()), number_candies, max_candies)
        elif item == '4':
            print("\nBye")
            quit()
        else:
            print("Invalid! Try Again\n")
            continue

        print(f"\nWinner - {win}")
        print("==========================")


game(221, 28)