n = int(input(""))
lst = list(map(int, input(). split()))
new = []

for i in lst:
    new.append(i**2)
print(*new)