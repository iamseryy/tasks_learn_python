from math import sqrt

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


x1 = int(input("Enter A point x-coordinate: "))
y1 = int(input("Enter A point y-coordinate: "))
x2 = int(input("Enter B point x-coordinate: "))
y2 = int(input("Enter B point y-coordinate: "))

print(f"A({x1, y1}); B({x2, y2}) -> {round(sqrt((x2 - x1)**2 + (y2 - y1)**2), 3)}")