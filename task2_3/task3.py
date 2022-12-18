#     Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
#
#     Пример:
#
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}


n = int(input("Enter a number: "))

if n > 0:
    numbers = []
    for i in range(n):
        numbers.append((1 + 1 / (i + 1)) ** (i + 1))
    print(f"for {[round(num, 2) for num in numbers]}\nsum = {round(sum(numbers), 2)}")
else:
    print("A number must be greater than zero")
