# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X /\ ¬Y /\ ¬Z для всех значений предикат.

isCorrectly = True

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            if not (x or y or z) != (not x) and (not y) and (not z):
                isCorrectly = False
                break

print("statement ¬(X ⋁ Y ⋁ Z) = ¬X /\ ¬Y /\ ¬Z : " + str(isCorrectly))