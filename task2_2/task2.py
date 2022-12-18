#     Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
#     Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


n = int(input("Enter a number: "))

if n > 0:
    mult = 1
    print(f"n = {n}, [ 1", end='')
    for i in range(2, n + 1):
        mult *= i
        print(f", {mult}", end='')
    print(" ]")
else:
    print("A number must be greater than zero")