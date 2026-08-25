""" Software 1 Exercise 5"""

talents = float(input("Enter talents:"))
pounds = float(input("Enter pounds:"))
lots = float(input("Enter lots:"))
weight = ((talents*20+pounds)*32+lots)*0.0133   # weight in kg
print(f"The weight in modern units:\n{int(weight):d} kilograms and {1000.0*(weight-int(weight)):.2f} grams.")
