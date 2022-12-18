# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# 
# Пример:
# 
# - 6 -> да
# - 7 -> да
# - 1 -> нет


day = int(input("Enter a day of week: "))
print(f"{day} -> {'yes' if day == 6 or day == 7 else 'no' if day > 0 and day < 8 else 'It is not a day of the week'}")