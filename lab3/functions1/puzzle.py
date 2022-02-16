def solve(numheads, numlegs):
    num1 = (4*numheads - numlegs)//2
    num2 = numheads - num1
    return num1, num2
numheads, numlegs = map(int, input().split())
print(solve(numheads, numlegs))