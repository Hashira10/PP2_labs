a = int(input())
b = map(int, input().split(maxsplit=a))
numbers = []
for i in b:
    numbers.append(i)
numbers.sort(reverse = True)
print(numbers[0]*numbers[1])