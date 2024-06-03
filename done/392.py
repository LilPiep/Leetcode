sub = "abc"
test = "ahbgdc"

sub2 = "axc"

sub3 = "acb"

def isSubsequence(s,t):
    if len(s) > len(t) : return False
    checkpoint = 0
    for i in range(len(s)):
        if i < len(s) and checkpoint == len(t): return False
        current = s[i]
        for j in range(checkpoint, len(t)):
            if t[j] == current:
                checkpoint = j + 1
                break
            if j == len(t)-1:
                return False
    return True

print(isSubsequence(sub3,test))