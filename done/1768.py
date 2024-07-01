def mergeAlternately(word1, word2):
    n = min(len(word1),len(word2))
    ans = ""
    for i in range(n):
        ans += word1[i]
        ans += word2[i]
    ans += word1[n:] + word2[n:]
    return ans

print(mergeAlternately("abc","pqr"))