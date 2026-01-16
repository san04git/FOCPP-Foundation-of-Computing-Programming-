import sys

def grep(pattern, filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if pattern in line:
                    print(line.rstrip())
    except FileNotFoundError:
        print(f"File not found: {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python grep.py pattern filename")
    else:
        grep(sys.argv[1], sys.argv[2]) 