temp = input("Enter temperature (e.g. 25C): ")

value = float(temp[:-1])
fahrenheit = (value * 9 / 5) + 32

print(str(fahrenheit) + "F") 