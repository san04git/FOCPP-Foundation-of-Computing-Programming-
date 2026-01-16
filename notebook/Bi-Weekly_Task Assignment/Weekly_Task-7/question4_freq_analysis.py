from collections import Counter

def most_common_letters(message, n=6):
    # Convert to lowercase and filter letters only
    filtered = [ch for ch in message.lower() if ch.isalpha()]
    counts = Counter(filtered)
    return counts.most_common(n)

if __name__ == "__main__":
    msg = input("Enter the message to analyze: ")
    common = most_common_letters(msg)
    print("Six most common letters and counts:")
    for letter, count in common:
        print(f"{letter}: {count}") 