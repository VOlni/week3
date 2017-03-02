class A(object):
    def __init__(self):
        self.a = 1

    def x(self):
        return 'A.x'

    def y(self):
        return 'A.y'

    def z(self):
        return 'A.z'

    def r(self):
        return 'A.r'


class B(A):
    def __init__(self):
        super().__init__()
        self.a = 2
        self.b = 3

    def y(self):
        return 'B.y'

    def z(self):
        return 'B.z'

    def r(self):
        return 'B.r'


class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5

    def z(self):
        return 'C.z'

    def r(self):
        return 'C.r'


class D(C, B):
    def __init__(self):
        self.b = 7
        self.a = 8
        super().__init__()
        self.d = 6

    def r(self):
        return 'D.r'


d = D()
print(d.a)
print(d.b)
print(d.c)
print(d.d)
print(d.x())
print(d.y())
print(d.z())
print(d.r())