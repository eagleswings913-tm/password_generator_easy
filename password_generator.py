
import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'I', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
SYMBOLS = ['!', '  # ', '$', '%', '&', '(', ')', '*', '+']
password = ""

def random_choice_from_list(input_list):
    return random.choice(input_list)

num_letters = int(input("How many letters should your password have? : "))
num_symbols = int(input("How many symbols should your password have? : "))
num_numbers = int(input("How many numbers should your password have? : "))

for i in range(num_letters):
    # print(i)
    character = random_choice_from_list(LETTERS)
    password += character
for i in range(num_symbols):
    # print(i)
    character = random_choice_from_list(SYMBOLS)
    password += character
for i in range(num_numbers):
    # print(i)
    character = random_choice_from_list(NUMBERS)
    password += character
print(f'Your new password is : {password}')