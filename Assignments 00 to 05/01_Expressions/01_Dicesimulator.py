import random

NUM_SIDES = 6

def roll_dice():

    dice1 = random.randint(1, NUM_SIDES)
    dice2 = random.randint(1, NUM_SIDES)
    total = dice1 + dice2
    print(f"Dice 1: {dice1}, Dice 2 : {dice2}, Total: {total} ")

def main():
    dice1 = 10
    print(f"Dice1 in main() start as {dice1}")

    for _ in range(3):
        roll_dice()

        print(f"dice1 in main() is still {dice1}")


if __name__ == '__main__':
    main()