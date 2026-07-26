matrix1 = []
matrix2 = []

for i in range (3):
    row1 = list(map(int, input().split()))
    matrix1.append(row1)
input()
for j in range (3):
    row2 = list(map(int, input().split()))
    matrix2.append(row2)

matrix3 = []

for x in range(3):
    new_row = []
    for h in range(3):
        new_row.append(matrix1[x][h] * matrix2[x][h])
    matrix3.append(new_row)

for num in matrix3:
    print(*num)






