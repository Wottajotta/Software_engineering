import math

class NegativeNumberError(Exception):
    pass

def calculate_square_root(num):
    if num < 0:
        raise NegativeNumberError("Ошибка: нельзя вычислить квадратный корень из отрицательного числа.")
    return math.sqrt(num)

def calculate_factorial(num):
    if num < 0:
        raise NegativeNumberError("Ошибка: факториал нельзя вычислить для отрицательного числа.")
    if num == 0:
        return 1
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


try:
    print(f'Квадратный корень из 16: {calculate_square_root(16)}')
    print(f'Факториал числа 5: {calculate_factorial(5)}')
    print(f'Квадратный корень из -4: {calculate_square_root(-4)}')
except NegativeNumberError as e:
    print(e)

try:
    print(f'Факториал числа -3: {calculate_factorial(-3)}')
except NegativeNumberError as e:
    print(e)
