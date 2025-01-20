def findWordsContaining(self, words: List[str], x: str) -> List[int]:
    ans = []
    i = 0
    for w in words:
        if x in w:
            ans.append(i)
        i += 1
    return ans