BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

password1 = input("Enter new password: ")
password2 = input("Confirm password: ")

if password1 in BAD_PASSWORDS:
    print("Error: Password is too common")
elif password1 != password2:
    print("Error: Passwords do not match")
elif len(password1) < 8 or len(password1) > 12:
    print("Error: Password must be 8 to 12 characters long")
else:
    print("Password Set")