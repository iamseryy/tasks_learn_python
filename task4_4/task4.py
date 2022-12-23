#     Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#     многочлена и записать в файл многочлен степени k.
#
#     Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


def get_coefficients(n):
    return [randint(0, 10) for i in range(0, n + 1)]


def get_polynomial_items(coefficients):
    polynomial_items = []

    for i in range(len(coefficients) - 1, -1, -1):
        if coefficients[i] != 0:
            if i == 0:
                polynomial_items.append(f"{coefficients[i]}")
            elif i == 1:
                polynomial_items.append("x" if coefficients[i] == 1 else f"{coefficients[i]}*x")
            else:
                polynomial_items.append(f"x**{i}" if coefficients[i] == 1 else f"{coefficients[i]}*x**{i}")

    return polynomial_items


def get_polynomial(items):
    return " + ".join(items) + " = 0"


k = int(input("Enter a natural power of a number: "))

file = open('task4_4/file.txt', 'w')
file.write(get_polynomial(get_polynomial_items(get_coefficients(k))))
file.close()
