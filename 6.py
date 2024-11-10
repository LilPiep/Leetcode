def convert(s, numRows):
    pattern = [[]]
    x = 0
    y = 0
    for i in range(0, len(s)):
        pattern[x][y] = s[i]
        if i < numRows:
            x += 1
        else:
            x = 0
            y += 1
    print(pattern)

print(convert("PAYPALISHIRING", 3))