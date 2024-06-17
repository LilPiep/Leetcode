n = [2,0,2,1,1,0]

def sortColors(nums):
    i = 1
    while i < len(nums):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
        i += 1
    return(nums)

print(sortColors(n))