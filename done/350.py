def intersect(nums1, nums2):
    (Counter(nums1)&Counter(nums2)).elements()

print(intersect([1,2,2,1],[2,2]))