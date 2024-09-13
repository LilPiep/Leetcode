from collections import Counter

def minimumPushes(word):
    ans = 0
    push = Counter(word).most_common()
    for i in range(len(push)):
        ans += push[i][1] * (i//8 + 1)
    return ans

print(minimumPushes("aabbccddeeffgghhiiiiii"))