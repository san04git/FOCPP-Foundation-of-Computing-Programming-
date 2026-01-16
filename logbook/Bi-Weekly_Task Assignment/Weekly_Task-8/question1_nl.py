import sys

def nl(filename):
    try:
        with open(filename, 'r') as file:
            for i, line in enumerate(file, start=1):
                print(f"{i}: {line.rstrip()}")
    except FileNotFoundError:
        print(f"File not found: {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python nl.py filename")
    else:
        nl(sys.argv[1])