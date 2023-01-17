# Задача 31: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]


input_range = input("Enter the range separated by a space: ").split()
range_from = int(input_range[0])
range_to = int(input_range[1])

items = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
result = list(map(lambda item: item[0], list(filter(lambda item: range_from <= item[1] <= range_to, enumerate(items)))))

print(items)
print(result)