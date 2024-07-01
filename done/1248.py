def numberOfSubarrays(nums, k):
    n = len(nums)
    cnt = [0] * (n + 1)
    cnt[0] = 1
    ans = 0
    t = 0
    for v in nums:
        t += v & 1
        if t - k >= 0:
            ans += cnt[t - k]
        cnt[t] += 1
    return ans

print(numberOfSubarrays([1,1,2,1,1], 3))