def reverseWords(s):
    s.strip()
    a = s.split()
    tab = []
    for word in a:
        tab.append(word)
    tab.reverse()
    ans = ""
    for i in range(len(tab)):
        ans += tab[i] + " "
    return ans[:-1]

print(reverseWords("the sky is blue"))