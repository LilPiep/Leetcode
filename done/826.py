class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ans = 0
        options = {}
        for i in range(len(difficulty)):
            if profit[i] not in options or difficulty[i] < options[profit[i]]:
                options[profit[i]] = difficulty[i]
        sorted_profits = sorted(options.keys(), reverse=True)
        worker.sort(reverse=True)
        profit_index = 0
        for w in worker:
            while profit_index < len(sorted_profits) and options[sorted_profits[profit_index]] > w:
                profit_index += 1
            if profit_index < len(sorted_profits):
                ans += sorted_profits[profit_index]
        return(ans)