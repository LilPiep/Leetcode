def findMaxAverage(nums, k):
    wsum = sum(nums[:k])
    max = wsum
    for i in range(len(nums) - k):
        wsum = wsum - nums[i] + nums[i+k]
        if wsum > max:
            max = wsum
    return max / k 

print(findMaxAverage([0,1,1,3,3], 4))