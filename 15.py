def threeSum(nums):
    ans = []
    pt1 = 0
    pt2 = 1
    pt3 = 2
    for n in nums:
        pt1 += 1
        for r in nums[pt1:]:
            pt2 += 1
            if (0-n-r) in nums[pt2:]:
                ans.append([pt1, pt2, nums[pt2:].index(0-r-n)])
    return set(ans)

print(threeSum([-1,0,1,2,-1,-4]))