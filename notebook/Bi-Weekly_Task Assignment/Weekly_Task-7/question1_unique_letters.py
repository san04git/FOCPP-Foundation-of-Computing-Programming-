def unique_letters(s):
    # Convert string to a set (unique letters), then sort and return as list
    return sorted(set(s))

if __name__ == "__main__":
    text = input("Enter a string: ")
    print("Unique letters sorted:", unique_letters(text)) 