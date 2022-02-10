dic = {
    "ONE" : "1",
    "TWO" : "2",
    "THR" : "3",
    "FOU" : "4",
    "FIV" : "5",
    "SIX" : "6",
    "SEV" : "7",
    "EIG" : "8",
    "NIN" : "9",
    "ZER" : "0"
    }

def f(a, g, first, second, ans):
    for i in range(len(a)):
        if a[i] == "+": g = i

    for i in range(0,g,3):
        for j in dic.keys():
            if a[i:i+3] == j: first += dic[j]

    for i in range(g+1, len(a), 3):
        for j in dic.keys():
            if a[i:i+3] == j: second += dic[j]
    
    num = int(first) + int(second)

    for i in str(num):
        for j in dic.keys():
            if i == dic[j]:
                ans += j

    return ans


a = input()
first = second = ans = ""
print(f(a,0, first, second, ans))

