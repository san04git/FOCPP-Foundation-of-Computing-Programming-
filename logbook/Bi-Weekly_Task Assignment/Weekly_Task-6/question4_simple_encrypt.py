def simple_encrypt(message):
    no_spaces = message.replace(" ", "")
    return no_spaces[::-1]  # Reverse string

if __name__ == "__main__":
    msg = input("Enter a message to encrypt: ")
    encrypted = simple_encrypt(msg)
    print("Encrypted message:", encrypted)