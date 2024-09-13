def smallestDistancePair(nums, k):
    dist = [(a, b) for idx, a in enumerate(nums) for b in nums[idx + 1:]]
    for i in range(len(dist)):
        dist[i] = abs(dist[i][0] - dist[i][1])
    dist.sort()
    return dist[k-1]

print(smallestDistancePair([1,6,1],3))