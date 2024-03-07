test = [0,0,1,1,1,2,2,3,3,4]


def removeDuplicates(nums):
    count = 0
    to_delete = []
    if nums:
        count = 1
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            count += 1
        else:
            to_delete.append(nums[i])
    for value in to_delete:
        nums.remove(value)
    return count


print(removeDuplicates(test))
