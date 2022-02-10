import sys
L = list(map(int, sys.stdin.read().split()))
i = 1
c = L[1]
while i < L[0]:
    c ^= L[1] + 2*i
    i += 1
print(c)
