def frequencySort(nums):
    freq = Counter(nums)
    nums.sort(key=lambda x: (freq[x], -x))
    return nums

print(frequencySort([1,1,2,2,2,3]))