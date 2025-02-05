class Solution:
    def completeDict(self, s, d):
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        d1 = {}
        d2 = {}
        self.completeDict(s1,d1)
        self.completeDict(s2,d2)
        if d1 != d2:
            return False
        if sum(c1 != c2 for c1, c2 in zip(s1, s2)) > 2:
            return False
        return True