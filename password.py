import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
password_length = int(input("Enter the desired password length: "))
print("Generated Password:", generate_password(password_length))