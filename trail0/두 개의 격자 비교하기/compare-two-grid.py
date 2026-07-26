n, m = map(int, input().split())
matrix1 =[]
matrix2 = []

for i in range(n):
    row1 = list(map(int,input().split()))
    matrix1.append(row1)

for j in range(n):
    row2 = list(map(int,input().split()))
    matrix2.append(row2)
matrix3 =[]

for x in range(n):
    new_row = []
    for h in range(m):
        if matrix1[x][h] == matrix2[x][h]:
            new_row.append(0)
        else:
            new_row.append(1)
    matrix3.append(new_row)

for num in matrix3:
    print(*num)