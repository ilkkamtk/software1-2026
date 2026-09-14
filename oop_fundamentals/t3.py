from car import Car

car = Car("ABC-123", 142)

car.accelerate(100)

car.drive(1.5)

print(f"Travelled distance: {car.travelled_distance}")  # should print 150
