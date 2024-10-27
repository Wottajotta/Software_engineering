# Тема 8. Введение в ООП

Отчет по Теме #8 выполнил:

- Харченко Владислав Андреевич
- АИС-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ |---|
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        

my_car = Car("Toyota", "Corolla")
print(f" Im driving {my_car.make} {my_car.model}")

```
### Результат.
![Изображение](https://github.com/Wottajotta/Software_engineering/blob/Тема_6/pic/Lab8_1.png "8.1")
### Выводы.
Создаем класс с конструктором, объявляем переменные в конструкторе. Создаем экземпляр класса с атрибутами и выводим их в консоль.

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def drive(self):
        print(f" Im driving {self.make} {self.model}")
        

my_car = Car("Toyota", "Corolla")
my_car.drive()
```
### Результат.
![Изображение](https://github.com/Wottajotta/Software_engineering/blob/Тема_6/pic/Lab8_2.png "8.2")
### Выводы.
Реализован класс Car с конструктором, методом drive. Далее реализуем экземпляр класса Car в переменной my_car, передаем атрибуты класса и вызываем метод drive().


## Лабораторная работа №3
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def drive(self):
        print(f"Driving {self.make} {self.model}")
        

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
        
    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")


my_electric_car = ElectricCar("Tesla", "Model S", 75)
my_electric_car.drive()
my_electric_car.charge()
```

### Выводы.
Здесь реализуем родительский класс Car, дочерний класс ElectricCar. Далее наглядно показываем метод наследования между классами.

## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
```python
class Car:
    def __init__(self, make, model):
        self._make = make
        self.__model = model
        
    def drive(self):
        print(f"Driving a {self._make} {self.__model}")
    

my_car = Car("Toyota", "Corolla")
print(my_car._make)
my_car.drive()
```
### Результат.
![Изображение](https://github.com/Wottajotta/Software_engineering/blob/Тема_6/pic/Lab8_4.png "8.4")
### Выводы.
Реализуем класс Car. В нем находится конструктор с атрибутами двух типов - защищенный и приватный. Далее получаем доступ к защищенному атрибуту с помощью экземпляра класса и вызываем метод drive(). Наглядная работа инкапсуляции.

## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.
```python
class Shape:
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
shapes = [Rectangle(5, 3), Circle(4)]
for shape in shapes:
    print(shape.area())
```
### Результат.
![Изображение](https://github.com/Wottajotta/Software_engineering/blob/Тема_6/pic/Lab8_5.png "8.5")
### Выводы.
Наглядная работа полиморфизма в ООП. Создаем родительский класс Shape, в который помещаем пустой метод area. Далее реализуем два дочерних класса Rectangle и Circle, где переопределяем метод area. В конце выводим в консоль метод area у обоих классов с атрибутами.

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Weather:
    def __init__(self, date, temperature):
        self.date = date
        self.temperature = temperature
        
    def report(self):
        print(f"On {self.date}, the temperature was {self.temperature} degrees.")
        
        
weather_report = Weather("2024-05-01", 25)
weather_report.report()
```
### Результат.
![Изображение](https://github.com/Wottajotta/Software_engineering/blob/Тема_6/pic/Sam8_1.png "8.1")
### Выводы.
Реализован класс Weather с атрибутами даты и температуры. Внутри класса есть метод прогноза погоды. Создаем экземпляр класса и вызываем метод report().

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Weather:
    def __init__(self, date, temperature):
        self.date = date
        self.temperature = temperature
        
        
    def report(self):
        print(f"On {self.date}, the temperature was {self.temperature} degrees.")
        
    def date_report(self):
        print(f"The date is {self.date}.")
        
        
weather_report = Weather("2024-05-01", 25)
weather_report.report()
weather_report.date_report()
```
### Результат.
![Изображение](https://github.com/Wottajotta/Software_engineering/blob/Тема_6/pic/Sam8_2.png "8.2")
### Выводы.
К классу, определенному заданием выше, добавлен метод date_report, указывающий дату, исходя из атрибута экзмепляра класса.


## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Weather:
    def __init__(self, date, temperature):
        self.date = date
        self.temperature = temperature
        
        
    def report(self):
        print(f"On {self.date}, the temperature was {self.temperature} degrees.")
        
    def date_report(self):
        print(f"The date is {self.date}.")
        
class Forecast(Weather):
    def __init__(self, date, temperature, forecast):
        super().__init__(date, temperature)
        self.forecast = forecast

    def forecast_report(self):
        print(f"On {self.date}, the temperature will be {self.temperature} degrees, and the forecast is {self.forecast}.")
        
        
weather_report = Forecast("June 1", 70, "sunny")
weather_report.forecast_report()
```
### Результат.
![Изображение](https://github.com/Wottajotta/Software_engineering/blob/Тема_6/pic/Sam8_3.png "8.3")
### Выводы.
Реализовано наследование, путем дочернего класса Forecast.

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.


```python
class Weather:
    def __init__(self, date, temperature):
        self._date = date
        self._temperature = temperature
        
        
    def report(self):
        print(f"On {self._date}, the temperature was {self._temperature} degrees.")
        
    def date_report(self):
        print(f"The date is {self._date}.")
        
class Forecast(Weather):
    def __init__(self, date, temperature, forecast):
        super().__init__(date, temperature)
        self.__forecast = forecast

    def forecast_report(self):
        print(f"On {self._date}, the temperature will be {self._temperature} degrees, and the forecast is {self.__forecast}.")
        
        
weather_report = Forecast("June 1", 70, "sunny")
weather_report.forecast_report()
```
### Результат.
![Изображение](https://github.com/Wottajotta/Software_engineering/blob/Тема_6/pic/Sam8_4.png "8.4")
### Выводы.
Реализована инкапсуляция. Атрибуты date и degrees переведены в статус защищенных атрибутов, а forecast - в приватный.

## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class Figure:
    def perimetr():
        pass
    

class Square(Figure):
    def __init__(self, a):
        self.a = a
        
    def perimetr(self):
        return 4 * self.a
    

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        return self.a + self.b + self.c


figures = [Square(5), Triangle(3, 4, 5)]
for figure in figures:
    print(figure.perimetr())
```
### Результат.
![Изображение](https://github.com/Wottajotta/Software_engineering/blob/Тема_6/pic/Sam8_5.png "8.5")
### Выводы.
Работа полиморфизма на примере родительского класса Figure с методом perimetr и переопределение его в дочерних классах.

## Общие выводы по теме
ООП - фундаментальная тема для любого современного языка программирования. В данной теме были применены на практике "столпы" ООП, а именно:
- Наследование
- Полиморфизм
- Инкапсуляция
В дальнейшем познакомимся с абстракцием и рассмотрим её на практике.