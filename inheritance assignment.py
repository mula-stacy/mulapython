class Vehicle:

    def __init__(self, model, cost, color):
        self.model = model
        self.cost = cost
        self.color = color

    def cars(self):
        print(self.model, self.cost, self.color)


class Toyota(Vehicle):
    pass


toyota = Toyota("Camri", "2.5million", "grey")
toyota.cars()


class Suzuki(Vehicle):
    pass


suzuki = Suzuki("Alto", "1.5million", "maroon")
suzuki.cars()


class RangeRover(Vehicle):
    pass


rangeRover = RangeRover("V8", "6million", "black")
rangeRover.cars()
