n = int(input())
numbers = map(int,input().split())
new = []
for i in numbers:
    if i % 2 == 0:
        new.append(i)
new.reverse()
print(*new)

