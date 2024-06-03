test = ["dog","racecar","car"]
test2 = ["flower","flow","flight"]
test3 = ["",""]
test4 = ["ab", "a"]
test5 = ["flower","flower","flower","flower"]

"""
def longestCommonPrefix(strs):
    if len(strs) == 1 : return strs[0]
    ans = ""
    first = strs[0]
    if first == "" : return ans
    i = 0
    for word in strs[1:]:
        if len(word) >= (i + 1):
            if word[i] != first[i]:
                return ans
            ans += first[i]
            i += 1
    return ans
"""

def longestCommonPrefix(strs):
    first = strs[0]
    len_first = len(first)

    for word in strs[1:]:
        while first != word[0:len_first]:
            len_first -= 1
            if len_first == 0:
                return ""
            first = first[0:len_first]
    return first

print(longestCommonPrefix(test5))