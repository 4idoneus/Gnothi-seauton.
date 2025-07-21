# Password Generator Project
# This is a simple password generator that creates a random password based on user input for letters,
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Version
print("Easy Version")
pass_letters = []
pass_numbers = []
pass_symbols = []
for letter in range(nr_letters):
    temp = random.choice(letters)
    pass_letters.append(temp)
for number in range(nr_numbers):
    temp = random.choice(numbers)
    pass_numbers.append(temp)
for symbol in range(nr_symbols):
    temp = random.choice(symbols)
    pass_symbols.append(temp)
print(pass_letters)
print(pass_symbols)
print(pass_numbers)
print(f"Your password is {"".join(pass_letters)}{"".join(pass_symbols)}{"".join(pass_numbers)}.")

print("-------------------------------------------------------------------------------------------------")

# Hard Version
print("Hard Version")
password = []
pass_letters = []
pass_numbers = []
pass_symbols = []
for letter in range(nr_letters):
    temp = random.choice(letters)
    pass_letters.append(temp)
    password.append(temp)
for number in range(nr_numbers):
    temp = random.choice(numbers)
    pass_numbers.append(temp)
    password.append(temp)
for symbol in range(nr_symbols):
    temp = random.choice(symbols)
    pass_symbols.append(temp)
    password.append(temp)
random.shuffle(password)

print(pass_letters)
print(pass_symbols)
print(pass_numbers)
print(f"Your password is {"".join(password)}.")