
import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'I', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ""
character = ""
min_range = 2
max_range = 8

def random_choice_from_list(input_list):
    return random.choice(input_list)

def is_integer(input_string):
    try:
        int(input_string)
        return True
    except ValueError:
        print("Please enter an integer!")
        return False

def validate_number_range(input_number, min_rng, max_rng):
    if min_rng <= int(input_number) <= max_rng:
        return True
    else:
        print("Enter a number between {min_range} and {max_range}")
        return False

while True:
    num_letters = input(f"How many letters should your password have? ({min_range}-{max_range}): ")
    if is_integer(num_letters):
        num_letters = int(num_letters)
        if validate_number_range(num_letters, min_range, max_range):
            break

while True:
    num_symbols = input(f"How many symbols should your password have? ({min_range}-{max_range}): ")
    if is_integer(num_symbols):
        num_symbols = int(num_symbols)
        if validate_number_range(num_symbols, min_range, max_range):
            break

while True:
    num_numbers = input(f"How many numbers should your password have? ({min_range}-{max_range}): ")
    if is_integer(num_numbers):
        num_numbers = int(num_numbers)
        if validate_number_range(num_numbers, min_range, max_range):
            break

for i in range(num_letters):
    character = random_choice_from_list(LETTERS)
    password += character
character = ""
for i in range(num_symbols):
    character = random_choice_from_list(SYMBOLS)
    password += character
character = ""
for i in range(num_numbers):
    character = random_choice_from_list(NUMBERS)
    password += character

print(f'Your new password is : {password}')