import string
import random

print("Welcome to PyPassword Generator!")
letter_count = int(input("How many letters would you like in your password?\n"))
if letter_count < 1:
    exit("Invalid input!")

symbol_count = int(input("How many symbols would you like in your password?\n"))
if symbol_count < 1:
    exit("Invalid input!")

number_count = int(input("How many numbers would you like in your password?\n"))
if number_count < 1:
    exit("Invalid input!")

password = ""
for i in range(letter_count + symbol_count + number_count):
    while True:
        category = random.randrange(3)
        if category == 0 and letter_count > 0:
            break
        elif category == 1 and symbol_count > 0:
            break
        if category == 2 and number_count > 0:
            break
    
    if category == 0:
        letter_count -= 1
        password += string.ascii_letters[random.randrange(len(string.ascii_letters))]
    elif category == 1:
        symbol_count -= 1
        password += string.punctuation[random.randrange(len(string.punctuation))]
    else:
        number_count -= 1
        password += str(string.digits[random.randrange(len(string.digits))])

print(f"Here is your password: {password}")