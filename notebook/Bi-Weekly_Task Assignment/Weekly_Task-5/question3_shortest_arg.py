import sys

def main():
    args = sys.argv[1:]  # exclude program name
    if not args:
        print("No arguments provided.")
        return
    shortest = sorted(args, key=len)[0]
    print("Shortest argument:", shortest)

if __name__ == "__main__":
    main() 