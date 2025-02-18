class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1,2,5]
        if n < 4:
            return dp[n-1]
        dp = [0]*(n)
        dp[1] = 1 
        dp[2] = 2
        dp[3] = 5
        for i in range(4,n):
            dp[i] = dp[i-1]*2 + dp[i-3]
        return dp[n]