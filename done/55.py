def canJump(nums):
    tot = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= tot:
            tot = i
    return True if tot == 0 else False

print(canJump([2,3,1,1,4]))