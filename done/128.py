test = [0,3,7,2,5,8,4,6,0,1]

def longestConsecutive(nums):
    if nums == []:
        return 0
    nums.sort()
    print(nums)
    best = 1
    current = 1
    for i in range(len(nums) - 1):
        if nums[i+1] == nums[i]+1:
            current += 1
        if nums[i+1] != nums[i]+1 and nums[i+1] != nums[i]:
            if best < current:
                best = current
            current = 1
    if best < current:
        best = current
    return best

print(longestConsecutive(test))