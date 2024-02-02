from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    engine = 0

    def set_engine(self):
        self.engine = Engine()
        return self.engine




"""
создайте класс `Car`, наследник `Vehicle`
"""
