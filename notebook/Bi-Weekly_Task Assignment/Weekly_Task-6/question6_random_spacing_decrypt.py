def random_spacing_decrypt(encrypted_message, interval):
    # Extract every interval-th character starting at 0
    return encrypted_message[::interval]

if __name__ == "__main__":
    encrypted_msg = input("Enter encrypted message: ")
    interval = int(input("Enter interval used: "))
    decrypted_msg = random_spacing_decrypt(encrypted_msg, interval)
    print("Decrypted message:", decrypted_msg) 