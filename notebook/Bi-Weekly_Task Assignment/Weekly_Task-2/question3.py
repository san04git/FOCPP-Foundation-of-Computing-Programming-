students = int(input("How many students? "))
group_size = int(input("Required group size? "))

groups = students // group_size
leftover = students % group_size

if leftover == 1:
    print("There will be", groups, "groups with 1 student left over.")
else:
    print("There will be", groups, "groups with", leftover, "students left over.") 