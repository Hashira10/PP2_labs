def permutation(s, ans):
    if(len(s) == 0):
        print(ans)
    for i in range(len(s)):
        letter = s[i]
        left = s[0:i]
        right = s[i + 1:]
        next = left + right
        permutation(next, ans + letter + " ")
ans = ""
string = input().split()
permutation(string,ans)