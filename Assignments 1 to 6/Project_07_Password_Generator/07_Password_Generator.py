import random

print("Welcome to Password Generator!")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890._-#@!`~$%^&*()[]:;'<>,?/=|"

number = int(input("Amount of passwords to generate: "))

length = int(input("Enter the length of password: "))

if number > 1:
    print("\nHere are your passwords")
elif number == 1:
    print("\nHere is your password")

for pwd in range(number):
    password = ""
    for c in range(length):
        password += random.choice(chars)
    print(password)
