temps = []

for i in range(6):
    temp = input("Enter temperature (e.g. 20C): ")
    value = float(temp[:-1])
    temps.append(value)

print("Maximum:", max(temps))
print("Minimum:", min(temps))
print("Mean:", sum(temps) / len(temps))