def jump(nums):
    max = 0
    count = 0
    curr = 0
    for i in range(len(nums)-1):
        if i + nums[i] > max:
            max = i+nums[i]
        if i == curr: 
            curr,count=max,count+1 
    return count

print(jump([2,3,1,1,4]))