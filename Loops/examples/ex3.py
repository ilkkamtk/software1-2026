initial_height = float(input("Height in meters: "))

G = 9.81

time = 0
distance = 0

while initial_height - distance >= 0:
    distance = 0.5 * G * time**2
    time = time + 0.00001
    print(f"Current height {initial_height - distance}")

print(f"Time: {time}")
