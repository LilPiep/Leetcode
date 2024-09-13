def reverseVowels(s):
    inventory = []

    for i in range(len(s)):
        if s[i] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            inventory.append(i)
    pg = 0
    pd = len(inventory)-1
    s = list(s)
    while pd > pg:
        s[inventory[pg]], s[inventory[pd]] = s[inventory[pd]], s[inventory[pg]]
        pg += 1
        pd -= 1
    return ''.join(s)

print(reverseVowels("aA"))