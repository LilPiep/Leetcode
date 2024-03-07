nums1 = [1]
m = 1
nums2 = []
n = 0

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    if m == 0:
        return nums2
    elif n == 0:
        return nums1

    cpt = m + n
    ptm = 0
    ptn = 0
    r = []
    while cpt != 0:
        if nums1[ptm] < nums2[ptn] and nums1[ptm] != 0:
            r.append(nums1[ptm])
            ptm += 1
        else:
            r.append(nums2[ptn])
            ptn += 1
        cpt -= 1
    print(r)
    return r

def mergebetter(nums1, m, nums2, n):
    for j in range(n):
          nums1[m+j] = nums2[j]
    nums1.sort()
    
merge(nums1, m, nums2, n)