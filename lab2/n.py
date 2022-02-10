l = []
k = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        l.append(n)
for i in range(len(l)//2):
    k.append(l[i] + l[len(l)-i-1])
if len(l)%2 !=0:
    k.append(l[len(l)//2])
print(*k)

