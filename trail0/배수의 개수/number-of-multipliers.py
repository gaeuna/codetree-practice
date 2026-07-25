total3 = 0
total5 = 0
for i in range(10):
    a = int(input())
    if a % 3 == 0:
        total3 = total3 + 1
    if a % 5 == 0:
        total5 = total5 + 1
print(total3, total5, end=" ")