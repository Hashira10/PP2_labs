def histogram(l):
    k = ""
    for i in l:
        for j in range(int(i)):
            k+="*"
        print(k)
        k = ""
l = input().split()
histogram(l)