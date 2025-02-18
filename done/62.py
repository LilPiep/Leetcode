class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n
        for _ in range(m-1):
            current = [1] * n
            for i in range(1,n):
                current[i] = current[i-1] + dp[i]
            dp = current
        return dp[-1]
        