def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == "3" and nums[i+1] == "3":
            return True
            break
    return False
num = input().split()
print(has_33(num))