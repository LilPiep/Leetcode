test = [3, 2, 3]


def majorityElement(nums):
    count = {}
    max = 0
    indice = nums[0]
    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    for key in count:
        if count[key] > max:
            max = count[key]
            indice = key
    return indice


print(majorityElement(test))
