import random

from tabulate import tabulate


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        self.cars.sort(key=lambda car: car.travelled_distance, reverse=True)

        printable_cars = []
        for car in self.cars:
            printable_cars.append(vars(car))

        print(tabulate(printable_cars, headers="keys"))

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
