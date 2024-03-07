import re
test = "ab_a"


def isPalindrom(s):
    s = s.lower()
    s = re.sub(r'\W+', '', s)
    s = s.replace("_", "")
    s = [*s]
    size = len(s)
    endroit = []
    envers = []
    for i in range(0, (size // 2), 1):
        endroit.append(s[i])
    if size % 2 == 0:  # ok
        for j in range(size - 1, (size // 2) - 1, -1):
            envers.append(s[j])
    else:
        for j in range(size - 1, (size // 2), -1):
            envers.append(s[j])
    if endroit == envers:
        return True
    return False


print(isPalindrom(test))
