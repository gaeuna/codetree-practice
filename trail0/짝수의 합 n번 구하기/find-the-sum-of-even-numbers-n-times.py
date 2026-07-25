n = int(input())

for i in range(n):
    total = 0
    a, b = map(int,input().split())
    for j in range(a, b+1):
        if j % 2 == 0:
            total = total + j
    print(total)
