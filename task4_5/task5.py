# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.
from collections import OrderedDict
import collections


def get_terms(polynomial_in_string):
    terms = {}
    polynomial_in_string = polynomial_in_string.split("=")[0].strip()
    for term in polynomial_in_string.split("+"):
        if "-" in term:
            neg_terms = term.split("-")
            first_item = neg_terms.pop(0)
            if term[0: 1] != "-":
                terms[get_key(first_item)] = float(get_value(first_item))
            for neg_term in neg_terms:
                terms[get_key(neg_term)] = -float(get_value(neg_term))
        else:
            terms[get_key(term)] = float(get_value(term))

    return terms


def get_key(term):
    if "**" in term:
        return int(term.split("**")[1].strip())
    else:
        if "x" in term:
            return 1
        else:
            return 0


def get_value(term):
    if "x" in term:
        parts = term.split("*")[0].strip()
        return parts[0] if "x" not in parts[0] else "1"
    else:
        return term.strip()


def sum(pol1, pol2):
    terms1 = get_terms(pol1)
    terms2 = get_terms(pol2)

    max_key1 = sorted(terms1.keys(), reverse=True)[0]
    max_key2 = sorted(terms2.keys(), reverse=True)[0]

    sum_terms = {}
    for i in range(max_key1 if max_key1 > max_key2 else max_key2):
        sum_terms[i] = terms1.get(i, 0) + terms2.get(i, 0)

    return sum_terms

def to_str(terms):
    polynomial = ""
    for i in range(sorted(terms.keys(), reverse=True)[0], 1, -1):
        polynomial += str(terms[i]) + "*" + "x**" + str(terms.keys())

    return polynomial



polynomial1 = " 2*x**4 - 7*x**5 + 9*x**3 - 3*x**2 + 7 + 5*x = 0 "
polynomial2 = "x**4 + 2*x**5 + 2*x**3 + 7*x**2 = 0"

termss1 = get_terms(polynomial1)
# termss2 = get_terms(polynomial2)
#
print(termss1)
# print(sorted(termss1.keys(), reverse=True)[0])
# print(termss2)
# print(sum(polynomial1, polynomial2))
print(to_str(termss1))
