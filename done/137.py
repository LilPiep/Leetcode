def singleNumber(nums):
    a = set(nums)
    for n in a:
        if nums.count(n) == 1:
            return n

print(singleNumber([2,2,3,2]))