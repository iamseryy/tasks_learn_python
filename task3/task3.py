# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


x = int(input("Enter x-coordinate: "))
y = int(input("Enter y-coordinate: "))

if x == 0 and y != 0:
    result = "y-axis"
elif x != 0 and y== 0:
    result = "x-axis"
elif x == 0 and y == 0:
    result = "coordinate center"
elif x > 0 and y > 0:
    result = 1
elif x < 0 and y > 0:
    result = 2
elif x < 0 and y < 0:
    result = 3
elif x > 0 and y < 0:
    result = 4

print(f"x = {x}; y = {y} -> {result}")