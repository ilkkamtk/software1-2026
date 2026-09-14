from car import Car

car = Car("ABC-123", 142)

print(
    f"Registration number: {car.registration_number}, maximum speed: {car.maximum_speed}"
)


car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print(f"Current speed: {car.current_speed}")  # should print 142

car.accelerate(-200)

print(f"Current speed: {car.current_speed}")  # should print 0
