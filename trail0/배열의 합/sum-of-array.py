array1 = []

for i in range(4):
    row1 = list(map(int, input().split()))
    array1.append(row1)

for row in array1:
    total = 0
    for num in row:
        total = total + num
    print(total)
