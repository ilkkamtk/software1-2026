"""Software 1 While loops exercises"""
import math
import random

# Phase 1
n = 1
while n <= 1000:
    if n%3 == 0:
        print(n)
    n = n + 1

# Phase 2
prompt = "Give me inches?"
inch = float(input(prompt))
while inch >= 0:
    print(f"It is in centimeters: {inch*2.54:.1f}")
    inch = float(input(prompt))

# Phase 3
prompt = "Give a number?"
s = input(prompt)
if s != "":
    smallest = int(s)
    largest  = smallest
    while s != "":
        n = int(s)
        if n < smallest:
            smallest = n
        elif n > largest:
            largest = n
        s = input(prompt)
    else:
        print(f"The smallest number given was {smallest}, and the largest was {largest}")

# Phase 4
the_number = random.randint(1, 10)
prompt = "Try to guess the number?"
guess = int(input(prompt))
while guess != the_number:
    if guess > the_number:
        print("Too high")
    else:
        print("Too low")
    guess = int(input(prompt))
else:
    print("Correct")

# Phase 5
username = "python"
password = "rules"
n = 5
while n > 0:
    u = input("Give the username?")
    p = input("Give the password?")
    if u == username and p == password:
        print("Welcome")
        break
    n = n - 1
else:
    print("Access denied")

# Phase 6, see https://en.wikipedia.org/wiki/Monte_Carlo_method
N = int(input("How many random points to generate?"))
n = 0
i = 0
while i < N:
    x = random.uniform(-1., 1.)
    y = random.uniform(-1., 1.)

    if x**2 + y**2 < 1.:
        n = n + 1

    i = i + 1
pi = 4.*n/N
print(f"Pi is {pi}, error {math.pi - pi}")