def prime(n):
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                return False
        else:
            return True
l = list(map(int,input().split()))
print(list(filter(lambda x: prime(x), l)))