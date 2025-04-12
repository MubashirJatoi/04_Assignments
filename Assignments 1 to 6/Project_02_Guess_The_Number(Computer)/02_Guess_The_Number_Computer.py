import random

def guess(x):
    Random_Number = random.randint(1, x)
    guess = 0
    while guess != Random_Number:
        guess = int(input(f"Guess the number between 1 to {x}: "))
        if guess < Random_Number:
            print("Sorry your guess is too low :(")
        else:
            print("Sorry your guess is too high :(")
    print(f"🎉 Congratulation! You've Guessed the number {Random_Number} Correct! :)")

guess(10)