class Foo(object):
    a = [1]
    b = 'stringAttribute'

    def __init__(self):
        self.__c = {'inherited': 'object'}
        self.d = ()
        self.n = 5

    def __len__(self):
        return self.n


obj1 = Foo()
obj1.a.append(3)
print(Foo.a)
obj1.a = [2]
print(Foo.a)
obj1.b += " extended"
print(Foo.b)
type(obj1)
obj1.c = None
print(obj1.c)