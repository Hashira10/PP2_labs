a = int(input())
dic = {}
mx = 0

for i in range(a):
    key, value = input().split()
    if key not in dic.keys(): 
        dic[key] = value
    else: 
        dic[key] = str(int(dic[key]) + int(value))


for i in dic.keys():
    if int(dic[i]) > mx: 
        mx = int(dic[i])


for i in sorted(dic):
    if int(dic[i]) != mx:
        k = mx - int(dic[i])
        print(i + " has to receive " + str(k) + " tenge")
    else:
        print(i + " is lucky!")
