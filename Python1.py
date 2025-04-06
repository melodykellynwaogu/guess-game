import random

number = random.randint(1, 10)

for i in range(3):
    user = int(input("Guess the number (1-10): "))

    if user == number:
        print(f"Hurray! You guessed the number right, it's{number}.")
        break
    else: 
        print("Wrong guess. Try again!")

        if user != number:
            print(f"sorry, you've used all attemps. The  number was {number}.")