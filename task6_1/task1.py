# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


data = input("Enter the element, difference and number of elements separated by a space: ").split()
result = list(map(lambda n: int(data[0]) + n * int(data[1]), [n for n in range(int(data[2]))]))
print(result)


