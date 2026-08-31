positive_int = int(input("Enter a positive integer: "))

number = 0
while number <= positive_int:
    if number % 2 == 0:
        print(number)

    number = number + 1
