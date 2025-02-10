class Solution:
    def solve(self, index, digits, comb, ans, temp):
        if index == len(digits):
            ans.append(temp)
            return

        for ch in comb[int(digits[index])]:
            self.solve(index + 1, digits, comb, ans, temp + ch)

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        comb = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []
        self.solve(0, digits, comb, ans, "")
        return ans