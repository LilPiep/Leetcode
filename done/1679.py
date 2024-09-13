def maxOperations(nums, k):
    nums.sort()
    ans = 0
    left = 0
    right = len(nums) - 1
    while left < right:
        oe = nums[left] + nums[right]
        if oe == k:
            ans += 1
            left += 1
        if oe < k:
            left += 1
        else:
            right -= 1

    return ans

print(maxOperations([1,2,4,3],5))