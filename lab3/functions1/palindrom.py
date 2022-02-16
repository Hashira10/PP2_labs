def palindrom(l,k,h):
    for i in range(len(l)//2):
        k += l[i]
    for i in range(len(l)-1,len(l)//2-1,-1):
        h += l[i]
    if h == k:
        return True
    else:
        return False
k = h = ""
l = input()
print(palindrom(l,k,h))