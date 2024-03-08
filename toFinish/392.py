subsequence = "aaaaaa"
test = "bbaaaa"

def isSubsequence(s, t):
    start = 0
    for i in range(len(s)):
        check = 0
        for j in range(start, len(t)):
            if s[i] == t[j] and i < j:
                check = 1
                start = j
                break
        if check == 0:
            return False
    if check == 0:
        return False
    return True

print(isSubsequence(subsequence, test))