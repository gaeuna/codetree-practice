array = []
total = 0

for i in range(4):
    row = list(map(int,input(). split()))
    array.append(row)

for j in range(4):
    for x in range(j+1):
        total = total + array[j][x]
print(total)