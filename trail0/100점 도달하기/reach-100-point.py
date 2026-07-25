n = int(input())
for i in range(n, 101):
    if i >= 90:
        grade = "A"
    elif i >= 80:
        grade = "B"
    elif i >= 70:
        grade = "C"
    elif i >= 60:
        grade = "D"
    else:
        grade = "F"
    print(grade, end = " ")