#Phase 1:  Ask for name and age from the user and print them in a formatted string.

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
#print("Welcome", user_name, "!")


#Phase 2: Check age and simple commands
if user_age < 12:
    print(f"Unfortunately {user_name}, you are a minor and cannot use this program.")
else:
    print(f"Welcome, {user_name}! Let´s start the game.")
    print("\n¨¨¨¨¨ Menu ¨¨¨¨¨")
    print("Command choices: cook, dance, sing, guess, lopeta")
    print("\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

    while True:
        command = input("Enter a command: ").lower()

        if command == "lopeta":
            print("Shutting down the game. Goodbye!")
            break
        elif command == "cook":
            print("Hello there, I can cook a pizza!")

        elif command == "dance":
            print("I am dancing! d[^__^]b")
           
        elif command == "sing":
            print("I am singing (・O・)")

        elif command == "guess":
            print("The lucky number is: 9")
        else:
            print("Unknown command. Please try again.")

        print("\n¨¨¨¨¨ Menu ¨¨¨¨¨")
        print("Commands choices: greet, dance, sing, guess, lopeta")
        print("\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")