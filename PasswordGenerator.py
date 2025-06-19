import random
import string


def generate_password(length=12, use_letters=True, use_digits=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters  # a-z + A-Z
    if use_digits:
        characters += string.digits  # 0-9
    if use_symbols:
        characters += string.punctuation  # !@#$%^&*() etc.

    if not characters:
        return "Error: No character sets selected!"

    password = ''.join(random.choices(characters, k=length))
    return password


def get_user_input():
    try:
        length = int(input("Enter password length (e.g. 12): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    if not any([use_letters, use_digits, use_symbols]):
        print("You must select at least one character type!")
        return

    password = generate_password(length, use_letters, use_digits, use_symbols)
    print(f"\nGenerated Password: {password}")


if __name__ == "__main__":
    get_user_input()