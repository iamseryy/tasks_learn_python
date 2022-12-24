#     Вычислить число c заданной точностью d
#
#     Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math

d = float(input("Enter a precision: "))


print("pi = " + str(math.pi))
print(f"d = {d}, pi = {}")