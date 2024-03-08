test = [1, 1, 1, 2, 2, 2, 3, 3]


def removeDuplicates(nums):
    i = 0
    while i < len(nums):
        cpt = 1
        current = nums[i]
        for j in range(i + 1, len(nums)):
            if current == nums[j]:
                cpt += 1
        for j in range(0, cpt - 2):
            nums.remove(current)
            i -= 1
        i += cpt
    print(nums)
    return len(nums)


print(removeDuplicates(test))
