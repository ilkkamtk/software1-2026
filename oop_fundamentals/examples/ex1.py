class Cycle:
    def __init__(self, new_wheel_count, new_brake_type, new_gear_count, new_color):
        self.wheel_count = new_wheel_count
        self.brake_type = new_brake_type
        self.gear_count = new_gear_count
        self.color = new_color
        self.speed = 0

    def accelerate(self, value):
        self.speed += value


bike_1 = Cycle(3, "disc", 5, "blue")


print(
    bike_1.wheel_count, bike_1.brake_type, bike_1.gear_count, bike_1.color, bike_1.speed
)

bike_1.accelerate(20)

print(bike_1.speed)
