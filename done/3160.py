class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        answer = []
        keepTrack = {}
        color_count = {}

        for q in queries:
            key, color = q
            if key in keepTrack:
                old_color = keepTrack[key]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:  
                    del color_count[old_color]
            keepTrack[key] = color  
            color_count[color] = color_count.get(color, 0) + 1  
            answer.append(len(color_count))
        return answer
