s = ["h","e","l","l","o"]
for i in range(len(s)//2):
    s[i], s[~i] = s[~i], s[i]