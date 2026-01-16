sweets = int(input("How many sweets are there? "))
pupils = int(input("How many pupils are present? "))

each = sweets // pupils
left = sweets % pupils

print("Each pupil gets", each, "sweets.")
print("Sweets left over:", left) 