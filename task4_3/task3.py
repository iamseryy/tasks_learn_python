# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint


def distinct(source):
    target = []

    for item in source:
        if item not in target:
            target.append(item)

    return target


n = 10
numbers = [randint(1, 5) for i in range(n)]

print(numbers)
print(distinct(numbers))