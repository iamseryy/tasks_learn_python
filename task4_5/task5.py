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
        parts = term.split("*")
        return parts[0].strip() if "x" in parts else "1"
    else:
        return term.strip()


def sum(pol1, pol2):
    terms1 = get_terms(pol1)
    terms2 = get_terms(pol2)

    max_key1 = sorted(terms1.keys(), reverse=True)[0]
    max_key2 = sorted(terms2.keys(), reverse=True)[0]

    sum_terms = {}
    for i in range((max_key1 if max_key1 > max_key2 else max_key2) + 1):
        sum_terms[i] = terms1.get(i, 0) + terms2.get(i, 0)

    return sum_terms


def to_str(terms):
    polynomial = ""
    terms_amount = sorted(terms.keys(), reverse=True)[0]
    for i in range(terms_amount, -1, -1):
        polynomial += (" - " if str(terms[i])[0:1] == "-" else (" + " if i < terms_amount else "")) \
                      + (str(abs(terms[i])) if abs(terms[i]) != 1 else "") \
                      + ("*" if i > 0 and abs(terms[i]) != 1 else "") \
                      + ("x**" if i > 1 else ("x" if i == 1 else "")) \
                      + (str(i) if i > 1 else "")

    polynomial += " = 0"

    return polynomial


file = open('task4_5/polynomial1.txt')
polynomial1 = file.read()
file.close()

file = open('task4_5/polynomial2.txt')
polynomial2 = file.read()
file.close()

file = open('task4_5/sum_polynomial.txt', 'w')
file.write(to_str(sum(polynomial1, polynomial2)))
file.close()
