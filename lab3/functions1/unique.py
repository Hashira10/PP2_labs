def unique(l):
    k = []
    for i in l:
        if i not in k:
            k.append(i)
    print(*k)
l = input().split()
unique(l)