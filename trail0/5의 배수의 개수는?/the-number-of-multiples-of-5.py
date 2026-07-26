array = []
for i in range(4):
    row = list(map(int, input().split()))
    array.append(row)
    
cnt = 0

for row in array :
    for num in row:
        if num % 5 == 0:
            cnt = cnt + 1
print(cnt)
            