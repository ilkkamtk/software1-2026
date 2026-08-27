"""Software 1 Condition exercises"""

# Phase 1
zander_limit = 42
zander_length = int(input("Give the size of zander (in cm)?"))
if zander_length < zander_limit:
    print(f"Return the fish into the lake. Length is {zander_limit-zander_length}cm less than required")

# Phase 2
cabin_class = input("Enter the cabin class?").upper()
if cabin_class == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("Above the car deck, equipped with a window")
elif cabin_class == "B":
    print("Windowless cabin above the car deck")
elif cabin_class == "C":
    print("Windowless cabin below the car deck")
else:
    print("Invalid cabin class")

# Phase 3
gender = input("What is your gender (F/M)").upper()
hemoglobin = int(input("What is your hemoglobin value (g/l)"))
if gender == "M":
    hemo_low = 134
    hemo_high = 167
else:
    hemo_low = 117
    hemo_high = 155

if hemoglobin < hemo_low:
    result = "low"
elif hemoglobin>=hemo_low and hemoglobin<=hemo_high:
    result = "normal"
else:
    result = "high"
print("Your hemoglobin level is " + result)

# Phase 4
year = int(input("Give the year?"))
if year%4 == 0 and (year%100 != 0 or year%400 == 0):
    print("This year is a leap year")
else:
    print("This year is not a leap year")