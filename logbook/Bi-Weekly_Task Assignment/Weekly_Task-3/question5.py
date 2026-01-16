BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password1 = input("Enter new password: ")
    password2 = input("Confirm password: ")

    if password1 in BAD_PASSWORDS:
        print("Password too common. Try again.")
    elif password1 != password2:
        print("Passwords do not match. Try again.")
    elif len(password1) < 8 or len(password1) > 12:
        print("Password must be 8 to 12 characters long.")
    else:
        print("Password Set")
        break