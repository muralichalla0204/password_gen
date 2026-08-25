import secrets
import string


def generate_password(length=12):
    if length < 2:
        raise ValueError("Password length must be at least 4")

    uppercase = secrets.choice(string.ascii_uppercase)
    lowercase = secrets.choice(string.ascii_lowercase)
    digit = secrets.choice(string.digits)
    special = secrets.choice(string.punctuation)

    all_characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    remaining = [
        secrets.choice(all_characters)
        for _ in range(length - 2)
    ]

    password = [uppercase, lowercase, digit, special] + remaining

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


if __name__ == "__main__":
    length = int(input("Enter password length: "))

    try:
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError as e:
        print("Error:", e)