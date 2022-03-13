def count(string,cnt1,cnt2):
    for i in string:
        if ord(i)>=65 and ord(i)<=90:
            cnt1 += 1
        if ord(i) >= 97 and ord(i) <= 122:
            cnt2 += 1
    print(cnt1,cnt2)

string = input()
count(string,0,0)