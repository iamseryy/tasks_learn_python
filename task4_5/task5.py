# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.


polynomial1 = "2*x**5 + 7*x**4 + 9*x**3 + 3*x**2 + 5*x + 7 = 0"
polynomial2 = "x**4 + 2*x**4 + 2*x**3 + 7*x**2 = 0"

coof1 = polynomial1.split("+")
coof1[len(coof1) - 1] = coof1[len(coof1) - 1][0:len(coof1[len(coof1) - 1]) - 4]
print(coof1)

polynomial_item = "".join(coof1[0].split("*x")).split("**")
if len(polynomial_item) == 2:
    polynomial1_max_degree = polynomial_item[1]
else:
    polynomial1_max_degree = 1

# polynomial_lenght = polynomial_item[0]
print(polynomial1_max_degree)