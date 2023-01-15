# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.
# все числа в диапазоне от 0 до 9
# И их количество соответственно тоже

def encode(data):
    if not data:
        return ''

    prev_char = ''
    count = 0
    result = ''

    for curr_char in data:
        if prev_char and curr_char != prev_char:
            result += f'{count}{prev_char}'
            count = 0

        count += 1
        prev_char = curr_char
    return f'{result}{count}{prev_char}'


def decode(code):
    if not code:
        return ''

    if code.isdigit():
        multipliers = list(filter(lambda i: i[0] % 2 == 0, list(enumerate(code))))
        values = list(filter(lambda i: i[0] % 2 != 0, list(enumerate(code))))
        return ''.join([int(multipliers[i][1]) * values[i][1] for i in range(len(multipliers))])
    else:
        mult = ''
        decode_val = ''
        for char in code:
            if char.isdigit():
                mult += char
            else:
                decode_val += int(mult) * char
                mult = ''
        return decode_val


source_encode_data = open('task5_4/source_encode.txt')
target_encode_data = open('task5_4/target_encode.txt', 'w')
source_decode_data = open('task5_4/source_decode.txt')
target_decode_data = open('task5_4/target_decode.txt', 'w')

target_encode_data.write(' '.join([encode(source) for source in source_encode_data.read().split()]))
target_decode_data.write(' '.join([decode(source) for source in source_decode_data.read().split()]))

source_encode_data.close()
source_decode_data.close()
source_decode_data.close()
target_decode_data.close()