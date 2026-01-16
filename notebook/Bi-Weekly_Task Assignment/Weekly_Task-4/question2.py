def count_letters(text):
    upper = 0
    lower = 0
    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    return upper, lower

# Test
text = input("Enter a string: ")
u, l = count_letters(text)
print("Uppercase:", u)
print("Lowercase:", l) 