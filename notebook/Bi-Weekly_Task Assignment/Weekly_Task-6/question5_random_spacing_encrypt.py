import random
import string

def random_spacing_encrypt(message):
    interval = random.randint(2, 20)
    encrypted_chars = []

    for char in message:
        encrypted_chars.append(char)
        # Add random letters after each char except last one
        for _ in range(interval - 1):
            encrypted_chars.append(random.choice(string.ascii_lowercase))

    encrypted_message = "".join(encrypted_chars)
    return encrypted_message, interval

if __name__ == "__main__":
    msg = input("Enter a message to encrypt: ")
    encrypted_msg, interval = random_spacing_encrypt(msg)
    print(f"Encrypted message: {encrypted_msg}")
    print(f"Interval used: {interval}") 