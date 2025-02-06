class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        l = len(nums)
        freq = {}
        tot = 0
        for i in range(l):
            for j in range(i + 1, l):
                product_value = nums[i] * nums[j]
                if product_value in freq:
                    freq[product_value] += 1
                else:
                    freq[product_value] = 1
        for f in freq.values():
            pair = (
                (f - 1) * f // 2
            )
            tot += 8 * pair
        return tot