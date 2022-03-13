string = input()
l = []
k = []
for i in string:
    l.append(i)
for i in reversed(l):
    k.append(i)
if l == k:
    print("Palindrom")
else:
    print("NO")