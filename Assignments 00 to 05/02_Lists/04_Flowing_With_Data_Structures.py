def add_three_copies(List_add, data):
    for i in range(3):
        List_add.append(data)


def main():
    message = input("Enter a message to copy: ")
    new_list = []
    print(f"List before: {new_list}")
    add_three_copies(new_list, message)
    print(f"List after: {new_list}")

if __name__ == '__main__':
    main()