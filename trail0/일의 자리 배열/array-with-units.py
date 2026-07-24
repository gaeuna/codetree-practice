num1, num2 = map(int,input().split())
list = [num1, num2]

for i in range(8):
    list.insert(i+2,list[i]+list[i+1])
    list[i+2] = list[i+2] % 10
print(*list)
    


