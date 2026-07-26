matrix = []
for i in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

final_matrix = []

for j in range(3):
    new_row = []
    for x in range(3):
        new_row.append(matrix[j][x]*3)
    final_matrix.append(new_row)
    
for num in final_matrix:
    print(*num)

