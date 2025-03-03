class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            min_value = min(nums)
            min_pos = nums.index(min_value)
            nums[min_pos] *= multiplier
        return nums