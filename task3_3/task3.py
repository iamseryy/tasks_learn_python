# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
#     Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


from random import uniform

n = 6
numbers = [round(uniform(0.0, 100.0), 3) for i in range(n)]
print(f"source = {numbers}")

fractionals = [round(numbers[i] - int(numbers[i]), 3) for i in range(len(numbers)) if numbers[i] - int(numbers[i]) != 0]
print(f"result = {round(max(fractionals) - min(fractionals), 4)}")
