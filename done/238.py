def productExceptSelf(nums):
    n = len(nums)
    a, b = 1, 1
    ans = [0]*n
    for i in range(n):
        ans[i] = a
        a *= nums[i]
    for i in range(n-1,-1,-1):
        ans[i] *= b
        b *= nums[i]
    return ans

print(productExceptSelf([1,2,3,4]))