class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        d = {}
        for i in range(len(groupSizes)):
            current = groupSizes[i]
            if current == 1:
                ans.append([i])
                pass
            if current in d:
                if len(d[current]) == current - 1:
                    d[current].append(i)
                    ans.append(d[current])
                    d[current] = []
                else:
                    d[current].append(i)
            else:
                d[current] = [i]
        return ans