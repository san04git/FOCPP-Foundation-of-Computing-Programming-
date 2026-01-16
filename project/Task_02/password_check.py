# --------------------------------------------
# Password Security Check Program (Task 2)
# --------------------------------------------
# This program reads passwords from a file
# and performs a 3-character security check
# if the password is long enough (>= 9 characters)
# --------------------------------------------

import sys           # To read command-line arguments
import random        # To generate random positions

# Function to display program header
def display_title():
    print("Password Security Check Program")
    print("=" * 40)

# Function to read passwords from a file
def read_passwords(filename):
    passwords = []  # List to store passwords

    try:
        with open(filename, "r") as file:
            # Read each line in the file
            for line in file:
                password = line.strip()  # Remove whitespace
                if password != "":
                    passwords.append(password)  # Add non-empty password
    except FileNotFoundError:
        print("Error: File not found.")
        return None

    return passwords

# Function to check a single password
def check_password(password):
    # Check password length
    if len(password) < 9:
        print(f"Password '{password}' is too short.\n")
        return

    print(f"Checking password: {password}")

    # Perform 3 random character checks
    for i in range(3):
        position = random.randint(1, len(password))  # 1-based position
        user_input = input(f"Enter letter at position {position}: ")

        # Compare input with correct character
        if user_input == password[position - 1]:
            print("Correct")
        else:
            print("Security check failed.\n")
            return  # Exit if incorrect

    # If all checks pass
    print("Security check passed.\n")

# Main function
def main():
    display_title()

    # Check command-line argument
    if len(sys.argv) < 2:
        print("Usage: python password_check.py <filename>")
        return

    filename = sys.argv[1]

    # Read passwords from file
    passwords = read_passwords(filename)
    if passwords is None:
        return

    # Process each password in file
    for pwd in passwords:
        check_password(pwd)

# Run the program
if __name__ == "__main__":
    main() 