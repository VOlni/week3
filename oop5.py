class Animal(object):
    def __init__(self, predator, weight, height=None):
        self.weight = weight
        self.predator = predator

    def eat(self):
        if self.predator:
            return 'I eat herbivores'
        else:
            return 'I eat herbs'


class Mammal(Animal):
    def __init__(self, lifespan, predator, weight, height):
        super().__init__(predator, weight, height)
        self.lifespan = lifespan

    def eat(self):
        return super().eat() + ', I am mammal'


class Raccoon(Mammal):
    def __init__(self, color, predator=True):
        self.color = color
        self.predator = predator

    def eat(self):
        return super().eat() + ', I am raccoon'


class Chupacabra(Raccoon):
    pass
