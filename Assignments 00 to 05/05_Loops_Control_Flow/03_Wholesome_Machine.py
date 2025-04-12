def main():
    message = "Please type the following affirmation: "
    print(message)
    affirmation = "I am capable of doing anything I put my mind to"
    print(affirmation)
    answer = str(input(""))

    while answer != affirmation:
        print("Hmmm That was not the affirmation")
        print(message)
        print(affirmation)
        answer = str(input("try again: "))
    print("That's right! :)")

if __name__ == '__main__':
    main()