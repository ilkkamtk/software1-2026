positive_int = int(input("Enter a positive integer: "))

if positive_int > 0:
    number = 0
    while number <= positive_int:
        if number % 2 == 0:
            print(number)

        number = number + 1
else:
    print("Positive integers only!")
