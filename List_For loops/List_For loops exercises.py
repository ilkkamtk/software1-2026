"""Software 1 List and For loops Exercise"""
import math
import random

# Phase 1
n = int(input("How many dices to roll?")) #the question asks how many dices, so I just fix the text in the input 
dice_sum = 0
for i in range(n):
    dice = random.randint(1, 6)
    print(str(dice), end=" ")
    dice_sum = dice_sum + dice
print(f"\nThe sum of the dices is: {dice_sum}")

# Phase 2
numbers = []
prompt = "Give me a number?"
s = input(prompt)
while s != "":
    numbers.append(float(s))
    s = input(prompt)
numbers.sort(reverse=True)
print(numbers[0:5])

# Phase 3
# https://en.wikipedia.org/wiki/Primality_test
n = int(input("Give the number?"))
for i in range(2, int(math.sqrt(n))+1):
    if n%i == 0:
        print(f"Dividable by {i}")
        break
else:
    print("It is a prime number")

# Phase 4
cities = []
for n in range(5):
    cities.append(input("Give me the name of the city"))
for city in cities:
    print(city)