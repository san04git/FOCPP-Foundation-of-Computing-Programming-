name = input("Enter your name: ")

if name == "":
    print("Hello, Stranger!")
else:
    name = name.lower()
    name = name[0].upper() + name[1:]
    print("Hello,", name)