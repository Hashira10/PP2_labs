def mult(l,ans):
    for i in l:
        ans *= int(i)
    return ans
string = input().split()
l = []
for i in string:
    l.append(i)
print(mult(l,1))