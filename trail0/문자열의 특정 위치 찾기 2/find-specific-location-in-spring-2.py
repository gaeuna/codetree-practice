list = ["apple", "banana", "grape", "blueberry", "orange"]
str = str(input())
cnt = 0

for x in list:
    if x[2] == str or x[3] == str:
        cnt = cnt + 1
        print(x)
print(cnt)
