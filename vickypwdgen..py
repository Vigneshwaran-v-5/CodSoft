import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    while True:
        pwd = ''.join(random.choice(characters) for _ in range(min_length))

        if numbers and not any(char.isdigit() for char in pwd):
            continue  
        if special_characters and not any(char in special for char in pwd):
            continue  

        return pwd

def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'n']:
            return response == 'y'
        print("Please enter 'y' or 'n'.")

min_length = int(input("Enter the minimum length for the password: "))
has_number = get_yes_no_input("Do you want to include numbers? (y/n): ")
has_special = get_yes_no_input("Do you want to include special characters? (y/n): ")

pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)
