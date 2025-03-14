class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 : return 0
        ans = 1
        current = s[0]
        for i in range(1, len(s)):
            current += s[i]
            if len(set(current)) == len(current) and len(current) > ans:
                ans += 1
            else:
                current = current[1:]
        return ans
