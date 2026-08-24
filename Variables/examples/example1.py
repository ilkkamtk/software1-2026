import math

radius = float(input("Enter the radius of the circle: "))
side = float(input("Enter the side length of the square: "))

circle_area = math.pi * radius**2
square_area = side * side

print(f"Area of the circle is {circle_area:.2f}")
print(f"Area of the square is {square_area:.2f}")
