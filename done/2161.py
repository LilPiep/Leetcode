class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = []
        for i in range(nums.count(pivot)):
            ans.append(pivot)
        pointer = 0
        for n in nums:
            if n < pivot:
                ans.insert(pointer, n)
                pointer += 1
            elif n > pivot:
                ans.append(n)
        return ans
