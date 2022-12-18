# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


n = abs(int(input("Enter a number: ")))

numbers = []

for i in range(-n, n + 1):
    numbers.append(i)
print(numbers)

file = open('task2_4/file.txt')

mult = 1
is_right_positions_exist = False

print("positions = ", end='')
for line in file:
    num = int(line)
    print(num, end='; ')
    if 0 <= num < len(numbers):
        is_right_positions_exist = True
        mult = mult * numbers[num]

file.close()

print(f"\nresult = {mult if is_right_positions_exist else 0}")
