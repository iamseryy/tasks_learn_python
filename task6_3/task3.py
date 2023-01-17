# Задача 32:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
# с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def custom_pow(num, p):
    if num == 0 and p < 0:
        return 'Error'
    elif p == 0:
        return 1
    elif p == 1:
        return num
    elif p == -1:
        return 1 / num
    elif p > 1:
        return num * custom_pow(num, p - 1)
    elif p < -1:
        return (1 / num) * custom_pow(num, p + 1)


a = int(input("Enter a number: "))
b = int(input("Enter a pow: "))

print(f"Result = {custom_pow(a, b)}")