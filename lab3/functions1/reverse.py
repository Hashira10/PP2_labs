def reverse_list(a):
    l = []
    for i in range(len(a)-1,-1,-1):
        l.append(a[i])
    print(*l)
string = input().split()
reverse_list(string)