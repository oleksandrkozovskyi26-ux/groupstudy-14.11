class Station:
    def __init__(self, name):
        self.name = name
        self.bikes = []

    def add_bike(self, bike):
        self.bikes.append(bike)

    def remove_bike(self, bike):
        self.bikes.remove(bike)
    
    def count_bikes(self):
        return len(self.bikes)