nums = input()
point = len(nums)-1
ok=True
for i in range(len(nums)-2,-1,-1):
    if int(nums[i])+i >= point:
        point = i
        ok=True
    else:
        ok=False               
print(ok)