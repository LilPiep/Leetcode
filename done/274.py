class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)
        while n > 0:
            oe = 0
            for c in range(n):
                if citations[c] >= n:
                    oe += 1
            if oe == n:
                return(n)
            n -= 1
        return(n)