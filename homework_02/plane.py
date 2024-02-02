from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, max_cargo):
        self.max_cargo = max_cargo

    def load_cargo(self, new_cargo):
        if new_cargo+self.cargo <= self.max_cargo:
            self.cargo = new_cargo
            return self.cargo
        else:
            msg = "Too much cargo"
            raise CargoOverload(msg)

    def remove_all_cargo(self):
        cargo_before = self.cargo
        self.cargo = 0
        return cargo_before

"""
создайте класс `Plane`, наследник `Vehicle`
"""
