test1 = [2,1,2]

def oe(nums):
    nums.sort()
    numTracker = 0
    minIncreament = 0

    for num in nums:
        numTracker = max(numTracker, num)
        minIncreament += numTracker - num
        numTracker += 1
    return minIncreament

print(oe(test1))