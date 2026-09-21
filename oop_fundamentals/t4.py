import random
from tabulate import tabulate

from car import Car

# create an empty list
cars = []

# for loop, loop 10 times (range)
for i in range(10):
    # randomise max speed 100-200 (randint)
    max_speed = random.randint(100, 200)
    # create registration number (use i)
    reg_num = f"ABC-{i + 1}"
    # create new car
    car = Car(reg_num, max_speed)
    # append car to list
    cars.append(car)


race_distance = 0
# while loop until someone wins the race (travelled distance of one of the cars is > 10000)
while race_distance < 10000:
    # loop the car list
    for car in cars:
        # set the speed of the car (accelerate between -10 and 15)
        car.accelerate(random.randint(-10, 15))
        # drive each car 1 hour (drive(1))
        car.drive(1)
        # (optional) order the list based on distance
        # check if distance of one of the cars is over 10000 if so, end while
        if car.travelled_distance >= 10000:
            race_distance = car.travelled_distance


# print the results (list) somehow ( then with e.g. tabulate library)

cars.sort(key=lambda car: car.travelled_distance, reverse=True)

printable_cars = []
for car in cars:
    printable_cars.append(vars(car))

print(tabulate(printable_cars, headers="keys"))
