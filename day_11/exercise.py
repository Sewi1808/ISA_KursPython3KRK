class Shape:
    pass


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


a = 10
b = 20
foo = Rectangle(a, b)
foo2 = Square(10)
print("a: \n", foo.a)
print("b: \n", foo.b)
print("Rectangle Area: \n", foo.area())
print("Square Area: \n", foo2.area())
