a = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
b = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
c = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

grades = a + b + c
grades = [4 if grade == 3 else grade for grade in grades if grade != 2]

print(f"Оценки после обработки: {grades}")
