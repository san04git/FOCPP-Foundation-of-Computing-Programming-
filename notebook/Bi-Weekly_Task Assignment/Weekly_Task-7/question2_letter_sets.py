def union_letters(w1, w2):
    return sorted(set(w1) | set(w2))  # Letters in either word

def intersection_letters(w1, w2):
    return sorted(set(w1) & set(w2))  # Letters in both words

def symmetric_diff_letters(w1, w2):
    return sorted(set(w1) ^ set(w2))  # Letters in one but not both

if __name__ == "__main__":
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")

    print("Letters in at least one word:", union_letters(word1, word2))
    print("Letters in both words:", intersection_letters(word1, word2))
    print("Letters in either but not both:", symmetric_diff_letters(word1, word2)) 