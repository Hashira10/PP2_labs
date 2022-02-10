n = int(input())
dig, up, low = 0, 0, 0
l = []
for i in range(n):
    k = input()
    for j in k:
        if j.isdigit():
            dig += 1
        elif j.isupper():
            up += 1
        elif j.islower():
            low += 1
    if dig > 0 and up > 0 and low > 0 and k not in l:
        l.append(k)
    dig = up = low = 0
l.sort()
print(len(l))
for i in l:
    print(i)
