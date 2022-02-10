dic = dict()
l = []
while True:
    a = input().split()
    if a[0] == "0":
        break
    if a[1] == "12":
        day = float(a[0]) + 365 + float(a[2])*365
    else:
        day = float(a[0]) + float(a[1])*30.5 + float(a[2])*365
    dic[str(day)] = a
    l.append(day)
l.sort()
for i in l:
    print(*dic[str(i)])