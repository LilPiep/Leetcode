class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(path):
            if len(path) == n:
                result.append("".join(path))
                return
            for char in "abc":
                if not path or path[-1] != char:
                    backtrack(path + [char])

        result = []
        backtrack([])
        
        return result[k-1] if k <= len(result) else ""