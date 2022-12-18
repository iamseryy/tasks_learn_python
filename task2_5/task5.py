# Реализуйте алгоритм перемешивания списка.

from random import randint


def mix(numbers):
    target_numbers = []
    indexes = []
    j = 0
    while j < n:
        index = randint(0, len(numbers) - 1)
        if indexes.count(index) == 0:
            indexes.append(index)
            j += 1

    for j in range(n):
        target_numbers.append(numbers[indexes[j]])

    return target_numbers


n = 10
source_numbers = []

for i in range(n):
    source_numbers.append(i)

print(f"Source - {source_numbers}")
print(f"Target - {mix(source_numbers)}")
