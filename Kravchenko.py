class Bicycle():
    def __init__(self, number):
        self.number = number

class Electric_bike(Bicycle):
    def rent(self, time):
        return 5 * time

class Regular_bike(Bicycle):
    def rent(self, time):
        return 2 * time