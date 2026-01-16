def remove_last_char(text):
    if len(text) <= 1:
        return text
    return text[:-1]

# Test
text = input("Enter a string: ")
print(remove_last_char(text))