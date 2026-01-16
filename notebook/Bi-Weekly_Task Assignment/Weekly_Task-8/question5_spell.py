import sys
import string

def load_dictionary():
    return set([
        "the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
        "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
        "this", "but", "his", "by", "from", "they", "we", "say", "her",
        "she", "or", "an", "will", "my", "one", "all", "would", "there",
        "their"
    ])

def spell_check(filename, dictionary):
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
            for p in string.punctuation:
                text = text.replace(p, '')
            words = text.split()

            unknown_words = set()
            for word in words:
                if word not in dictionary:
                    unknown_words.add(word)

            if unknown_words:
                print("Words not in dictionary:")
                for word in sorted(unknown_words):
                    print(word)
            else:
                print("No unknown words found.")
    except FileNotFoundError:
        print(f"File not found: {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python spell.py filename")
    else:
        dictionary = load_dictionary()
        spell_check(sys.argv[1], dictionary) 