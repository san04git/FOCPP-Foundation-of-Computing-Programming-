number = int(input("Enter a number between 0 and 12: "))

if 0 <= number <= 12:
    for i in range(13):
        print(i, "x", number, "=", i * number)
else:
    print("Invalid number") 