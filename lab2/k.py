a = input()
h = a.split()
s = []
for i in h:
    if i.isalpha():
        if i not in s:
            s.append(i)
    else:
        if i not in s:
            s.append(i[:-1])
s.sort()
print(len(s))
for i in s:
    print(i)