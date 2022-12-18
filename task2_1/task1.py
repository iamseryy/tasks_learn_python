#     Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
#     Пример:
#
# - 6782 -> 23
# - 0,56 -> 11


parts = input("Enter a number: ").split(".")
part1 = abs(int(parts[0]))

total = 0

if len(parts) == 2:
    part2 = int(parts[1])
    while part2 != 0:
        total += part2 % 10
        part2 //= 10

while part1 != 0:
    total += part1 % 10
    part1 //= 10


print("Sum = " + str(total))