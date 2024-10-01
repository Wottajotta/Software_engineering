import math

def calculate_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Такой треугольник не существует.")

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
