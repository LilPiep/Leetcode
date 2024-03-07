s = "foo"
t = "bar"

''''
def isIsomorphic(s, t):
    d1 = {}
    i = 1
    group = s[0]
    while i < (len(s)):
        while s[i] == s[i - 1]:
            group += s[i]
            i += 1
        if group not in d1:
            d1[group] = 1
        else:
            d1[group] += 1
        group = s[i]
        i += 1
    d2 = {}
    i = 0
    group = ""
    while i < (len(t) - 2):
        group = t[i]
        while t[i] == t[i + 1]:
            group += t[i + 1]
            i += 1
        if group not in d2:
            d2[group] = 1
        else:
            d2[group] += 1
        i += 1
    print(d1, d2)
    l1 = []
    l2 = []
    for key in d1:
        l1.append(d1[key])
    for key in d2:
        l2.append(d2[key])
    if l1 == l2:
        return True
    return False


print(isIsomorphic(s, t))
'''''


def isIsomorphic(s, t):
    d1 = {}
    for i in range(len(s)):
        if s[i] not in d1:
            d1[s[i]] = [i]
        else:
            d1[s[i]].append(i)
    d2 = {}
    for i in range(len(t)):
        if t[i] not in d2:
            d2[t[i]] = [i]
        else:
            d2[t[i]].append(i)
    l1 = []
    l2 = []
    for key in d1:
        l1.append(d1[key])
    for key in d2:
        l2.append(d2[key])
    if l1 == l2:
        return True
    return False


print(isIsomorphic(s, t))
