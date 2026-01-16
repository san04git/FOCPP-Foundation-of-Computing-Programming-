import sys

def main():
    # sys.argv contains the program name + arguments
    # We exclude the program name itself by subtracting 1
    arg_count = len(sys.argv) - 1
    print(f"Number of arguments provided: {arg_count}")

if __name__ == "__main__":
    main()