def longestSubarray(nums, limit):
    
    left = 0
    max_length = 0
    
    current_max = nums[0]
    current_min = nums[0]
    
    for right in range(len(nums)):
        current_max = max(current_max, nums[right])
        current_min = min(current_min, nums[right])
        
        if current_max - current_min > limit:
            left += 1
            current_max = max(nums[left:right+1])
            current_min = min(nums[left:right+1])
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

print(longestSubarray([8,2,4,7], 4))