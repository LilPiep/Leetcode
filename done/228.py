test = [0, 1, 2, 4, 5, 7]


def summaryRanges(nums):
    nums.append(0)
    fleche = "->"
    res = []
    i = 1
    if len(nums) == 1:
        return res
    if len(nums) == 2:
        res.append(str(nums[0]))
        return res
    while i < len(nums):
        borne_min = nums[i - 1]
        borne_max = nums[i - 1]
        while nums[i - 1] + 1 == nums[i]:
            borne_max = nums[i]
            i += 1
        if borne_min == borne_max:
            res.append(str(borne_min))
        else:
            res.append(str(borne_min) + fleche + str(borne_max))
        i += 1
    return res


print(summaryRanges(test))
