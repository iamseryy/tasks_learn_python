# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
#     Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint
from math import ceil

n = 6
numbers = [randint(-100, 100) for i in range(n)]

print(f"source = {numbers}")
print(f"target = {[numbers[i] * numbers[len(numbers) - i - 1] for i in range(ceil(len(numbers) / 2))]}")
