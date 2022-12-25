#     Вычислить число c заданной точностью d
#
#     Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

d = input("Enter a precision: ")

if 0.0000000001 <= float(d) <= 0.1:
    print("pi = " + str(math.pi))
    print(f"d = {float(d)}, pi = {round(math.pi, len(d.split('.')[1]))}")
else:
    print("Precision must be in the range [10^{-1}, 10^{-10}]")
