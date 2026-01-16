password1 = input("Enter new password: ")
password2 = input("Confirm password: ")

if password1 != password2:
    print("Error: Passwords do not match")
elif len(password1) < 8 or len(password1) > 12:
    print("Error: Password must be 8 to 12 characters long")
else:
    print("Password Set")