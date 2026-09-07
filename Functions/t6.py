import math


def price_of_pizza_unit(diameter, price):
    area = math.pi * (diameter / 100 / 2) ** 2
    return price / area


pizza1 = price_of_pizza_unit(30, 14)
pizza2 = price_of_pizza_unit(40, 24)

if pizza1 < pizza2:
    print(f"Pizza 1 is {100 - 100 * pizza1 / pizza2:.0f}% cheaper")
else:
    print(f"Pizza 2 is {100 - 100 * pizza2 / pizza1:.0f}% cheaper")
