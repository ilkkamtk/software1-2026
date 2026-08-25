""" Software 1 Exercise 5"""
import random 

print(f"First combination lock number {random.randint(0, 999):03d}")
s = str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6))
print("Second combination lock number " + s)