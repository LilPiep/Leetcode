def searchInsert(nums, target) -> int:
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)