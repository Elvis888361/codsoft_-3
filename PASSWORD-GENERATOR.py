import random
import string

# Function to generate a random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get the desired length of the password from the user
while True:
    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length <= 0:
            raise ValueError("Password length must be a positive integer.")
        break
    except ValueError as e:
        print(e)
        continue

# Generate and display the password
password = generate_password(password_length)
print(f"Your generated password is: {password}")
