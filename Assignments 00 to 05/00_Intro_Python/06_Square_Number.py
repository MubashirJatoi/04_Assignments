def main():

    number : float = float(input("\033[1;3m Type a number to see its square: \033[0m"))
    square : float = number * number
    print(f"{number} squared is {square}")

if __name__ == '__main__':
    main()