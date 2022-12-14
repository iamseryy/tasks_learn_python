# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Enter quarter of coordinate plane: "))

if quarter == 1:
    result = "(X > 0; Y > 0)"
elif quarter == 2:
    result = "(X < 0; Y > 0)"
elif quarter == 3:
    result = "(X < 0; Y < 0)"
elif quarter == 4:
    result = "(X > 0; Y < 0)"
else:
    result = "It is a not quarter of coordinate plane"

print(f"quarter = {quarter} -> {result}")