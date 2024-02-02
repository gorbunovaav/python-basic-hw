import exceptions


class Vehicle:
    started = True
    weight = 0
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self, started):
        if not started and self.fuel > 0:
            started = True
            return started
        else:
            msg = "No fuel :("
            raise exceptions.LowFuelError(msg)

    def move(self, distance):
        required_fuel = self.fuel_consumption * distance
        if self.fuel >= required_fuel:
            self.fuel -= required_fuel
            return self.fuel
        else:
            msg = "Not enough fuel :("
            raise exceptions.NotEnoughFuel(msg)


