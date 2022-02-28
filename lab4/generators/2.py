n = int(input())
for i in range(0,n+1,2):
    if i != n and i != n-1:
        print(i, end = ",")
    else:
        print(i)

'''
l = []
def gen(n):
    for i in range(n+1):
        if i % 2 == 0:
            l.append(i)
    for i in range(len(l)):
        if i != len(l)-1:
            print(l[i],end = ",")
        else:
            print(l[i])
n = int(input())
gen(n)

'''
