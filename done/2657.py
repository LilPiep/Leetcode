class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        track = []
        ans = []
        current = 0
        for i in range(len(A)):
            if (A[i] in track):
                current += 1
            else: 
                track.append(A[i])
            if (B[i] in track):
                current += 1
            else:
                track.append(B[i])
            ans.append(current)
        return ans