#     Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
#     Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def binary_integer(source):
    target = ""
    while source > 0:
        target = str(source % 2) + target
        source //= 2

    return int(target) if target != "" else 0


def binary(number, precision=0):
    parts = str(number).split(".")
    parts[0] = int(parts[0])

    target = str(binary_integer(parts[0]))

    if len(parts) == 1 or precision == 0:
        return target

    target += "."

    for i in range(precision):
        parts[1] = float('0.' + parts[1])
        parts = str(parts[1] * 2).split(".")
        target += parts[0]
    return target


num = float(input("Enter a number greater than or equal to zero: "))
if num - int(num) != 0:
    precis = int(input("Enter a precision: "))
    print(f"result = {binary(num, precis)}")
else:
    print(f"result = {binary(num)}")
