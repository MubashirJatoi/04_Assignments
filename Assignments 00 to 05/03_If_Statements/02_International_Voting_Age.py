def main():
    age : int = int(input("How old are you? "))
    if age >= 16 and age < 25:
        print("You can vote in Peturksbouipo where the voting age is 16.")
        print("You cannot vote in Stanlau where the voting age is 25.")
        print("You cannot vote in Mayengua where the voting age is 48.")
    elif age >= 25 and age < 48:
        print("You can vote in Stanlau where the voting age is 25.")
        print("You can also vote in Peturksbouipo where the voting age is 16.")
        print("But you cannot vote in Mayengua where the voting age is 48.")
    elif age >= 48:
        print("You can vote in Stanlau where the voting age is 25.")
        print("You can also vote in Peturksbouipo where the voting age is 16.")
        print("You can also vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in any country you are so young to vote sorry!  :(")


if __name__ == '__main__':
    main()