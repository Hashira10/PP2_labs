def spy_game(nums):
    for i in range(len(nums)):
        if nums[i] == '0':
            for j in range(i+1,len(nums)):
                if nums[j] == '0':
                    for k in range(j+1,len(nums)):
                        if nums[k] == '7':
                            return True
                            break
    return False
a = input().split()
print(spy_game(a))