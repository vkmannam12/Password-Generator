import random
import string

def generate_password(length=12):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_chars = letters + digits + symbols
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    print("Generated Password:", generate_password(length))
