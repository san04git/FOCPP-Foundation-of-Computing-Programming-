temps = []

while True:
    temp = input("Enter temperature (press Enter to stop): ")
    if temp == "":
        break
    value = float(temp[:-1])
    temps.append(value)

if temps:
    print("Maximum:", max(temps))
    print("Minimum:", min(temps))
    print("Mean:", sum(temps) / len(temps))
else:
    print("No temperatures entered") 