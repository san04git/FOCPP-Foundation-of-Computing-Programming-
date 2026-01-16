import sys

def main():
    temps = sys.argv[1:]
    if not temps:
        print("No temperature readings provided.")
        return

    try:
        temps_float = [float(t) for t in temps]
    except ValueError:
        print("All arguments must be numbers.")
        return

    maximum = max(temps_float)
    minimum = min(temps_float)
    mean = sum(temps_float) / len(temps_float)

    print(f"Max: {maximum}")
    print(f"Min: {minimum}")
    print(f"Mean: {mean:.2f}")

if __name__ == "__main__":
    main()