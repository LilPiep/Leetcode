n = [23,2,4,6,7]
k = 6

def checkSubarraySum(nums, k):
    m = {0: -1} 
    s = 0

    for i in range(len(nums)):
        s += nums[i]
        rem = s % k

        if rem in m:
            if i - m[rem] > 1:
                return True
        else:
            m[rem] = i

    return False

print(checkSubarraySum(n,k))