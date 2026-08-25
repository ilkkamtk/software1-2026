""" Software 1 Exercise 2"""
import math

radius = float(input("What's the radius of the circle?:"))
print(f"Area of the circle is {math.pi*radius**2:.1f}")

rectangle_length = float(input("What's the length of the rectangle?:"))
rectangle_width = float(input("What's the width of the rectangle?:"))
print(f"Perimeter is {2*rectangle_length+2*rectangle_width:.1f} and area is {rectangle_length*rectangle_width:.1f}")


