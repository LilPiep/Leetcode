def minKBitFlips(nums, k):
    n = len(nums)
    ans = flipped = 0
    isFlipped = [0]*n

    for i in range(n):
        if i >= k:
            flipped ^= isFlipped[i - k]
        if flipped == nums[i]:
            if i + k > n:
                return -1
            isFlipped[i] = 1
            flipped ^= 1
            ans += 1
    
    return ans

print(minKBitFlips([0,1,0],1))