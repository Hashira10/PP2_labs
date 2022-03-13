import time, math
def root(n,m):
    time.sleep(m*10**(-6))
    print("Square root of", n, "after", m, "milliseconds is", n**(1/2))
n = int(input())
m = int(input())
root(n,m)
