class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        self.dfs(candidates, 0, target, path, res)
        return res
    
    def dfs(self, candidates, cur, target, path, res):
        if target == 0:
            res.append(path.copy())
            return
        if target < 0:
            return
        
        for i in range(cur, len(candidates)):
            if i > cur and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            self.dfs(candidates, i + 1, target - candidates[i], path, res)
            path.pop()  