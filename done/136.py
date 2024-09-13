import functools

def singleNumber(nums):
    return functools.reduce(lambda x, y: x ^ y, nums, 0)

print(singleNumber([2,2,1]))