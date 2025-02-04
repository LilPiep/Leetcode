class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        best = 0
        current = 0
        prev = -1
        for num in nums:
            if num > prev:
                current += num
            else:
                best = max(best, current)
                current = num
            prev = num  
        return max(best, current)