
'''
class Vehicle(object):
    def __init__(self, milage):
        self.milage = milage

    def get_milage(self):
        milage = 630
        return self.milage

vehicle = Vehicle(530)
print(vehicle.get_milage())
#530
'''
'''
class Vehicle(object):
    def __init__(self, milage):
        self.milage = milage

    def add_milage(self, milage=100):
        self.milage += milage

    def get_milage(self):
        return self.milage


vehicle = Vehicle(530)
vehicle.add_milage()
vehicle.get_milage()
#1200
'''
'''
class Vehicle(object):
    def __init__(self, milage):
        self.milage = milage

    def add_milage(self, milage=100):
        self.milage += milage

    def get_milage(self):
        return self.milage


vehicle = Vehicle(530)
vehicle.add_milage(110)
vehicle.get_milage()
#630
'''
'''
class Vehicle(object):
    def __init__(self, milage):
        self.milage = milage

    def add_milage(self, milage=10):
        self.milage += milage

    def get_milage(self):
        return self.milage


vehicle_1 = Vehicle(700)
vehicle_2 = vehicle_1
vehicle_2.add_milage()
vehicle_1.get_milage()
#710
'''