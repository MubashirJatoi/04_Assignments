import random

def main():
    dice1 = random.randint(1, 6)
    print(f"dice1 = {dice1}")
    dice2 = random.randint(1, 6)
    print(f"dice2 = {dice2}")
    total = dice1 + dice2
    print(f"total of both dice is = {total}")
if __name__ == '__main__':
    main()