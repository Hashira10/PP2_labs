a = int(input())
arr = [[]]
for i in range(a):
    for j in range(a):
        if i == 0:
            print(j, end = " ")
        elif j == 0:
            print(i, end = " ")
        elif i == j:
            print(i*j, end = " ")
        else:
            print(0, end = " ")
    print()
