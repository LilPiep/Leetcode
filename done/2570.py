class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        track = {}
        for pair in nums1:
            track[pair[0]] = pair[1]
        for pair in nums2:
            if pair[0] in track:
                track[pair[0]] += pair[1]
            else:
                track[pair[0]] = pair[1]
        ans = sorted([[c, track[c]] for c in track])
        return ans