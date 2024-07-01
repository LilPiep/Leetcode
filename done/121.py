class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        mp = 0
        while sell < len(prices):
            cp = prices[sell]-prices[buy]
            if prices[buy] < prices[sell]:
                mp = max(cp, mp)
            else:
                buy = sell
            sell += 1
        return mp