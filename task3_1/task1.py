# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
#
#     Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

n = 5
numbers = [randint(-100, 100) for i in range(n)]

print(f"source = {numbers}")
print(f"sum = {sum([numbers[i] for i in range(1, len(numbers), 2)])}")

