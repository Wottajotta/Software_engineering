from add import calculate_area

def main():
    try:
        a = float(input("Введите длину первой стороны треугольника: "))
        b = float(input("Введите длину второй стороны треугольника: "))
        c = float(input("Введите длину третьей стороны треугольника: "))

        area = calculate_area(a, b, c)
        print("Площадь треугольника:", area)

    except ValueError as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    main()
