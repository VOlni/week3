a = 12
b = 15


class Rectangle(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_a(self):
        return a

    def get_b(self):
        return b


class Rhombus(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b


rectangle_1 = Rectangle(a, b)
rectangle_1.get_a()
rectangle_1.get_b()
rhombus_1 = Rhombus(a, b)
rhombus_1.get_a()
rhombus_1.get_b()
rhombus_2 = Rhombus(22, 25)
rhombus_2.get_a()
rhombus_2.get_b()
rectangle_2 = Rectangle(1, 2)
print(rectangle_2.get_a())
print(rectangle_2.get_b())
a = rectangle_1.get_a() + rhombus_1.get_a()
a
rectangle_1.get_a()
rhombus_1.get_a()
b = b + rectangle_2.get_b() + rhombus_2.get_b()
print(b)
print(rectangle_2.get_b())
print(rhombus_2.get_b())