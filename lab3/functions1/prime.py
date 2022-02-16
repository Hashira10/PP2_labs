def filter_prime(n):
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                break
        else:
            print(n)

import sys

num =  list(map(int, sys.stdin.read().split()))
for i in range(len(num)):
    filter_prime(num[i])

