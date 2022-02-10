a = int(input())
dic = dict()
dic2 = dict()

# dic[стихия] = колличество повторений в первом вводе
for i in range(a):
    demon = input().split()
    if demon[1] not in dic.keys(): dic[demon[1]] = 1
    else: 
        dic[demon[1]] = dic[demon[1]]+1

b = int(input())
cnt = 0

# dic[стихия] = число возможных убийств демона
for i in range(b):
    k = input().split()
    if k[1] not in dic2.keys(): dic2[k[1]] = k[2]
    else: 
        dic2[k[1]] = int(dic2[k[1]])+int(k[2])


for i in dic.keys():
    if i not in dic2.keys(): # если во 2 вводе нет данной стихии, то демон жив
        cnt += dic[i]
    for j in dic2.keys():
        if i == j:
            c = int(dic2[j]) - int(dic[i])  
            if c < 0:
                cnt += abs(c)
print("Demons left: " + str(cnt))