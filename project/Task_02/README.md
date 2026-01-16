# Password Security Check Program

## Description
This program reads passwords from a file and performs a 3-letter security check
for passwords that are 9 or more characters long. If the password is too short,
it is skipped. The program exits immediately if a user enters the wrong letter.

## How to Run
1. Open terminal
2. Navigate to project folder
3. Run the program:

   python password_check.py passwords.txt

## Input File
- One password per line
- Password must be at least 9 characters long

## Notes
- No third-party libraries required
- Program checks 3 random letters from each valid password
- Exits immediately on incorrect input 