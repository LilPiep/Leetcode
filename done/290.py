test = "abba"
sentence = "dog cat cat dog"


def wordPattern(pattern, s):
    s = s.split(" ")
    pattern = [*pattern]
    dpattern = {}
    dsentence = {}
    for i in range(len(pattern)):
        if pattern[i] not in dpattern:
            dpattern[pattern[i]] = [i]
        else:
            dpattern[pattern[i]].append(i)
    for i in range(len(s)):
        if s[i] not in dsentence:
            dsentence[s[i]] = [i]
        else:
            dsentence[s[i]].append(i)
    comp1 = []
    comp2 = []
    for key in dpattern:
        comp1.append(dpattern[key])
    for key in dsentence:
        comp2.append(dsentence[key])
    return comp1 == comp2


print(wordPattern(test, sentence))
