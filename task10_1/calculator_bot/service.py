def calculate(x, y, operation):
    return operation(x, y)


def get_number(num):
    if num.isdigit():
        number = int(num)
    elif is_float(num):
        number = float(num)
    elif is_complex(num):
        number = complex(num)
    else:
        number = False

    return number


def is_complex(number):
    try:
        number = complex(number)
        return True
    except ValueError:
        return False


def is_float(number):
    try:
        number = float(number)
        return True
    except ValueError:
        return False
