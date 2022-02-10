a = int(input())
l = []
l2 = []
for i in range(a):
    k = input().split()
    if k[0] == "1":
        l.append(k[1])
    elif k[0] == "2":
        l2.append(l[0])
        l.pop(0)
print(*l2)

