l = []
def my_func(a,b):
    if l[b] == -1:
        if(b >= len(a) - 1):
            l[b] = 1
        else:
            l[b] = 0
            for i in range(1,a[b] + 1):
                if а(a,b+i) == 1:
                    l[b] = 1
                    break
    return l[b]

a = list(map(int, input().split()))
for i in range(len(a)):
    l.append(-1)

print(my_func(a,0))





