def factors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    print("Factors:", factors(number)) 