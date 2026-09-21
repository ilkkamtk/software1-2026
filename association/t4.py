import random

from race import Race
from car import Car

cars = []
for i in range(10):
    cars.append(Car(f"ABC-{i+1}", random.randint(100, 200)))


race = Race("Grand Demolition Derby", 8000, cars)

hours = 0

while not race.race_finished():
    race.hour_passes()
    hours += 1
    if hours % 10 == 0:
        print(f"-------------STATUS hour {hours}--------------")
        race.print_status()

print(f"-------------RACE FINISHED--------------")
race.print_status()
