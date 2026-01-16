number = int(input("Enter a number: "))

if abs(number) <= 12:
    if number < 0:
        for i in range(12, -1, -1):
            print(i, "x", abs(number), "=", i * abs(number))
    else:
        for i in range(13):
            print(i, "x", number, "=", i * number)
else:
    print("Number must be between -12 and 12") 