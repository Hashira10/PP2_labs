a,b = map(int, input().split())
num = int(input())
dic = dict()
l = []
k = []
for i in range(num):
    g = input().split()
    c = ((int(g[0])-a)**2 + (int(g[1])-b)**2)**0.5
    dic[str(c)] = g
    l.append(c)

l.sort()
for i in l:
    print(*dic[str(i)])