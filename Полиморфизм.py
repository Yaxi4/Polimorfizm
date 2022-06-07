class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a

    def get_area(self):
        return self.a ** 2


class Circle:
    def __init__(self, a):
        self.a = a

    def get_area(self):
        return 3.14 * self.a ** 2


rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)
sq1 = Square(5)
sq2 = Square(7)
cir1 = Circle(3)
cir2 = Circle(2)

figures = [rect1, rect2, sq1, sq2, cir1, cir2]
for figure in figures:
    print(figure.get_area())
