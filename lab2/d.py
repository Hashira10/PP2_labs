a = int(input())
arr = [[]]
if a%2 !=0:
    for i in range(a):
        for j in range(a):
            if i + j >= a - 1:
                print("#", end="")
            else:
                print(".", end="")
        print()
if a%2==0:
    for i in range(a):
        for j in range(a):
            if i == j or i > j:
                print("#", end="")
            else:
                print(".", end="")
        print()
