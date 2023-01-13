# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def get_factors(number):
    factors = []
    factor = 2
    while factor * factor <= number:
        while number % factor == 0:
            factors.append(factor)
            number //= factor

        factor += 1

    if number > 1:
        factors.append(number)

    return factors


n = int(input("Enter a integer number greater than zero: "))
print(f"N = {n}")
print(get_factors(n))

