tab = [2, 2, 3]
value = 2


def removeElement(nums, val):
    count = 0
    for num in nums:
        if num != val:
            count += 1
    for i in range(len(nums) - count):
        nums.remove(val)
    return count, nums


print(removeElement(tab, value))
