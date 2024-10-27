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
        

    