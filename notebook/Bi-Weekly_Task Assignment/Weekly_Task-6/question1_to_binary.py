def to_binary(n):
    # Python has a built-in function bin() that converts int to binary string
    # bin(10) -> '0b1010', so we slice off the '0b'
    return bin(n)[2:]

if __name__ == "__main__":
    number = int(input("Enter a positive integer: "))
    print("Binary representation:", to_binary(number)) 