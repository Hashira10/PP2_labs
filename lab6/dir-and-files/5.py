f = open('test.txt', 'w')
string = input().split()
l = []
for i in string:
    l.append(i)
for i in l:
    f.write("%s\n" % i)
