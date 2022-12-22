#     Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
#     Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    if n == 0:
        return [0]

    if n == 1:
        return [1, 0, 1]

    fib_list_right = [0, 1]
    fib_list_left = [0, 1]

    for i in range(2, n + 1):
        fib_list_right.append(fib_list_right[i - 2] + fib_list_right[i - 1])
        fib_list_left.append(fib_list_left[i - 2] - fib_list_left[i - 1])

    fib_list_left.reverse()
    fib_list_left.pop()

    return fib_list_left + fib_list_right


print(fib(int(input("Enter a number: "))))
