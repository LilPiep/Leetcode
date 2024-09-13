def findDifference(nums1, nums2):
    ans = []
    keeptrack = []
    for n in nums1:
        if n not in nums2 and n not in keeptrack:
            keeptrack.append(n)
    ans.append(keeptrack)
    keeptrack = []
    for n in nums2:
        if n not in nums1 and n not in keeptrack:
            keeptrack.append(n)
    ans.append(keeptrack)
    return ans

print(findDifference([1,2,3], [2,4,6]))